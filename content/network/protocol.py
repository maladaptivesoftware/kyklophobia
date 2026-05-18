import struct
import socket
import numpy as np
from enum import IntEnum


class MessageType(IntEnum):
    JOIN            = 1
    UPDATE_POS      = 2
    BLOCK_CHANGE    = 3
    _SEED           = 10
    PLAYER_JOIN     = 11
    PLAYER_LEFT     = 12
    PLAYER_POS      = 13
    BLOCK_UPDATE    = 14
    PLAYER_LIST     = 15
    SV_MESSAGE      = 16
    MODS            = 17
    CHAT            = 18
    ITEM_SPAWN      = 20
    ITEM_DESPAWN    = 21
    ITEM_DROP       = 22
    ITEM_PICKUP     = 23
    ITEM_COLLECT    = 24
    SERVER_REQUEST  = 30
    SERVER_RESPONSE = 31
    DISCONNECT      = 32


MT = MessageType




def mkjoin(nm, tb=b'\x00' * 16):
    b = nm.encode('utf-8')
    return struct.pack('<B16sI', MT.JOIN, tb, len(b)) + b




def mkposupd(pos, yaw, pitch, _held=0, anim_flags=0):
    return struct.pack(
        '<B3f2fHB', MT.UPDATE_POS,
        float(pos[0]), float(pos[1]), float(pos[2]),
        float(yaw), float(pitch), _held, anim_flags
    )







def mkblockchg(x, y, z, bt):
    return struct.pack('<BiiiH', MT.BLOCK_CHANGE, x, y, z, bt)



def mkseed(seed):
    return struct.pack('<BI', MT._SEED, seed)



def mkpjoin(pid, nm, pos):
    b = nm.encode('utf-8')
    return struct.pack(
        '<BI3fI', MT.PLAYER_JOIN, pid,
        float(pos[0]), float(pos[1]),
        float(pos[2]), len(b)
    ) + b



def mkleft(pid):
    return struct.pack('<BI', MT.PLAYER_LEFT, pid)



def mkpos(pid, pos, yaw, pitch, _held=0, anim_flags=0):
    return struct.pack(
        '<BI3f2fHB', MT.PLAYER_POS, pid,
        float(pos[0]), float(pos[1]), float(pos[2]),
        float(yaw), float(pitch), _held, anim_flags
    )



def mkblockupd(x, y, z, bt):
    return struct.pack('<BiiiH', MT.BLOCK_UPDATE, x, y, z, bt)



def mkmods(mods):
    total = sum(len(cm) for cm in mods.values())
    d = struct.pack('<BII', MT.MODS, total, len(mods))
    
    for (cx, cz), cm in mods.items():
        d += struct.pack('<iiI', cx, cz, len(cm))
        for (lx, y, lz), bt in cm.items():
            d += struct.pack('<BBBH', lx, y, lz, bt)
            
            
    return d



def mklist(players):
    d = struct.pack('<BI', MT.PLAYER_LIST, len(players))
    for pid, pd in players.items():
        pos = pd['pos']
        nm  = pd.get('nm', f'Player{pid}')
        b   = nm.encode('utf-8')
        d += struct.pack(
            '<I3fI', pid,
            float(pos[0]), float(pos[1]),
            float(pos[2]), len(b)
        ) + b
        
    return d





def mkservmsg(msg):
    b = msg.encode('utf-8')
    return struct.pack('<BI', MT.SV_MESSAGE, len(b)) + b




def mkchat(msg):
    b = msg.encode('utf-8')
    return struct.pack('<BI', MT.CHAT, len(b)) + b



def mkitemspawn(eid, iid, cnt, pos, vel):
    return struct.pack(
        '<BIII3f3f', MT.ITEM_SPAWN, eid, iid, cnt,
        float(pos[0]), float(pos[1]), float(pos[2]),
        float(vel[0]), float(vel[1]), float(vel[2])
    )




def mkitemdespawn(eid):
    return struct.pack('<BI', MT.ITEM_DESPAWN, eid)




def mkitemdrop(iid, cnt, pos, vel):
    return struct.pack(
        '<BII3f3f', MT.ITEM_DROP, iid, cnt,
        float(pos[0]), float(pos[1]), float(pos[2]),
        float(vel[0]), float(vel[1]), float(vel[2])
    )
    
    
    
    

def mkitempick(eid):
    return struct.pack('<BI', MT.ITEM_PICKUP, eid)

def mkitemcollect(iid, cnt):
    return struct.pack('<BII', MT.ITEM_COLLECT, iid, cnt)

def mksvrq():
    return struct.pack('<B', MT.SERVER_REQUEST)






def mksvreply(nm, motd, cp, mp):
    nb = nm.encode('utf-8')
    mb = motd.encode('utf-8')
    return struct.pack(
        '<BIIII', MT.SERVER_RESPONSE,
        len(nb), len(mb), cp, mp
    ) + nb + mb



def mkdisconnect(reason=""):
    b = reason.encode('utf-8')
    return struct.pack('<BI', MT.DISCONNECT, len(b)) + b










class ReadMessage:
    def __init__(self, sock):
        self.sock   = sock
        self.buffer = b''


    def recv(self, needed=4096):
        data = self.sock.recv(needed)
        if data: self.buffer += data
        return data


    def _pull(self, n):
        # recv until buffer has n bytes
        
        while len(self.buffer) < n:
            try:
                d = self.sock.recv(max(4096, n - len(self.buffer)))
                if not d: return False
                self.buffer += d
                
                
            except (socket.error, OSError):
                return False
                
                
        return True







    def readmsg(self):
        if not self.buffer:
            try:
                self.sock.settimeout(0.1)
                d = self.sock.recv(4096)
                self.sock.settimeout(1.0)
                if not d: return None
                self.buffer += d
                
                
            except socket.timeout:
                self.sock.settimeout(1.0)
                return None
                
            except (socket.error, OSError):
                return None

        if not self.buffer: return None
        mt = self.buffer[0]
        
        
        
        

        # fixed-size messages
        _fixed = {                # B + *
            MT.UPDATE_POS:    24, # 3f(12) + 2f(8) + H(2) + B(1)
            MT.BLOCK_CHANGE:  15, # iii(12) + H(2)
            MT.BLOCK_UPDATE:  15,
            MT._SEED:          5, # I(4)
            MT.PLAYER_LEFT:    5,
            MT.ITEM_SPAWN:    37, # III(12) + 3f(12) + 3f(12)
            MT.ITEM_DESPAWN:   5,
            MT.ITEM_DROP:     33, # II(8) + 3f(12) + 3f(12)
            MT.ITEM_PICKUP:    5,
            MT.ITEM_COLLECT:   9, # II(8)
            MT.PLAYER_POS:    28, # I(4) + 3f(12) + 2f(8) + H(2) + B(1)
            MT.SERVER_REQUEST: 1,
        }
        
        
        

        if mt in _fixed:
            tl = _fixed[mt]
            if not self._pull(tl): return None
            d = self.buffer[:tl]
            self.buffer = self.buffer[tl:]
            return (mt, d)



        # B(1) + 16s + I(4) + nm
        if mt == MT.JOIN:
            if not self._pull(21): return None
            nl = struct.unpack('<I', self.buffer[17:21])[0]
            if not self._pull(21 + nl): return None
            d = self.buffer[1:21 + nl]
            self.buffer = self.buffer[21 + nl:]
            return (mt, d)



        #  B(1) + I(4) + 3f(12) + I(4) + nm
        if mt == MT.PLAYER_JOIN:
            if not self._pull(21): return None
            nl = struct.unpack('<I', self.buffer[17:21])[0]
            if not self._pull(21 + nl): return None
            d = self.buffer[1:21 + nl]
            self.buffer = self.buffer[21 + nl:]
            return (mt, d)



        # B(1) + I(4) + text
        if mt in (MT.SV_MESSAGE, MT.CHAT, MT.DISCONNECT):
            if not self._pull(5): return None
            ml = struct.unpack('<I', self.buffer[1:5])[0]
            if not self._pull(5 + ml): return None
            d = self.buffer[1:5 + ml]
            self.buffer = self.buffer[5 + ml:]
            return (mt, d)



        #  B + I(cnt) + [I + 3f + I + nm] * cnt
        if mt == MT.PLAYER_LIST:
            if not self._pull(5): return None
            cnt = struct.unpack('<I', self.buffer[1:5])[0]
            off = 5
            for _ in range(cnt):
                if not self._pull(off + 20): return None
                nl = struct.unpack('<I', self.buffer[off+16:off+20])[0]
                if not self._pull(off + 20 + nl): return None
                off += 20 + nl
            d = self.buffer[:off]
            self.buffer = self.buffer[off:]
            return (mt, d)



        #  B + I(total) + I(chunks) + [ii + I(cnt) + (BBB+H)*cnt]
        if mt == MT.MODS:
            if not self._pull(9): return None
            _, nc = struct.unpack('<II', self.buffer[1:9])
            off = 9
            for _ in range(nc):
                if not self._pull(off + 12): return None
                _, _, cnt = struct.unpack('<iiI', self.buffer[off:off+12])
                off += 12
                bs = cnt * 5
                if not self._pull(off + bs): return None
                off += bs
            d = self.buffer[:off]
            self.buffer = self.buffer[off:]
            return (mt, d)



        #  B + IIII + nm + motd
        if mt == MT.SERVER_RESPONSE:
            if not self._pull(17): return None
            nl, ml, _, _ = struct.unpack('<IIII', self.buffer[1:17])
            if not self._pull(17 + nl + ml): return None
            d = self.buffer[:17 + nl + ml]
            self.buffer = self.buffer[17 + nl + ml:]
            return (mt, d)


        self.buffer = self.buffer[1:]
        return None






    def parse_join(self, data):
        token = data[:16]
        nl    = struct.unpack('<I', data[16:20])[0]
        nm    = data[20:20+nl].decode('utf-8')
        return token, nm




    def parse_posupdate(self, data):
        x, y, z, yaw, pitch, _held, afl = struct.unpack('<3f2fHB', data[1:])
        return np.array([x, y, z], dtype='f4'), yaw, pitch, _held, afl



    def parse_blockchange(self, data):
        x, y, z, bt = struct.unpack('<iiiH', data[1:])
        return x, y, z, bt


    def parse_seed(self, data):
        return struct.unpack('<I', data[1:])[0]








    def parse_playerjoin(self, data):
        if len(data) < 20:
            raise ValueError(f"PLAYER_JOIN too short: {len(data)}")

        pid     = struct.unpack('<I', data[0:4])[0]
        x, y, z = struct.unpack('<3f', data[4:16])
        nl      = struct.unpack('<I', data[16:20])[0]
        nm      = data[20:20+nl].decode('utf-8', errors='replace')
        return pid, nm, np.array([x, y, z], dtype='f4')


    def parse_playerleft(self, data):
        return struct.unpack('<I', data[1:])[0]




    def parse_playerpos(self, data):
        pid             = struct.unpack('<I', data[1:5])[0]
        x, y, z, yaw, pitch, _held, afl = struct.unpack('<3f2fHB', data[5:])
        return pid, np.array([x, y, z], dtype='f4'), yaw, pitch, _held, afl




    def parse_blockupdate(self, data):
        x, y, z, bt = struct.unpack('<iiiH', data[1:])
        return x, y, z, bt





    def parse_mods(self, data):
        if len(data) < 9: raise ValueError("MODS too short")
        _, nc = struct.unpack('<II', data[1:9])
        mods  = {}
        off   = 9

        for _ in range(nc):
            if off + 12 > len(data): raise ValueError("chunk header missing")
            cx, cz, cnt = struct.unpack('<iiI', data[off:off+12])
            off += 12
            cm = {}

            for _ in range(cnt):
                if off + 5 > len(data): raise ValueError("block data missing")
                lx, y, lz = struct.unpack('<BBB', data[off:off+3])
                bt = struct.unpack('<H', data[off+3:off+5])[0]
                cm[(lx, y, lz)] = bt
                off += 5

            mods[(cx, cz)] = cm

        return mods




    def parse_list(self, data):
        cnt     = struct.unpack('<I', data[1:5])[0]
        players = {}
        off     = 5

        for _ in range(cnt):
            pid     = struct.unpack('<I', data[off:off+4])[0]
            x, y, z = struct.unpack('<3f', data[off+4:off+16])
            nl      = struct.unpack('<I', data[off+16:off+20])[0]
            nm      = data[off+20:off+20+nl].decode('utf-8')
            players[pid] = {'pos': np.array([x, y, z], dtype='f4'), 'nm': nm}
            off += 20 + nl

        return players




    def parse_svmsg(self, data):
        ml = struct.unpack('<I', data[:4])[0]
        return data[4:4+ml].decode('utf-8')



    def parse_chatmsg(self, data):
        ml = struct.unpack('<I', data[:4])[0]
        return data[4:4+ml].decode('utf-8')



    def parse_itemspawn(self, data):
        eid, iid, cnt, x, y, z, vx, vy, vz = struct.unpack('<III3f3f', data[1:])
        return eid, iid, cnt, np.array([x, y, z], dtype='f4'), np.array([vx, vy, vz], dtype='f4')



    def parse_itemdespawn(self, data):
        return struct.unpack('<I', data[1:])[0]




    def parse_itemdrop(self, data):
        iid, cnt, x, y, z, vx, vy, vz = struct.unpack('<II3f3f', data[1:])
        return iid, cnt, np.array([x, y, z], dtype='f4'), np.array([vx, vy, vz], dtype='f4')



    def parse_itempickup(self, data):
        return struct.unpack('<I', data[1:])[0]




    def parse_itemcollect(self, data):
        iid, cnt = struct.unpack('<II', data[1:])
        return iid, cnt




    def parse_svreplyinfo(self, data):
        nl, ml, cp, mp = struct.unpack('<IIII', data[1:17])
        nm   = data[17:17+nl].decode('utf-8')
        motd = data[17+nl:17+nl+ml].decode('utf-8')
        return {'nm': nm, 'motd': motd, 'current_players': cp, 'maxp': mp}




    def parse_disconnect(self, data):
        rl = struct.unpack('<I', data[:4])[0]
        return data[4:4+rl].decode('utf-8')
