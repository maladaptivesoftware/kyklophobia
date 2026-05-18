#version 330
in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;
in float in_part_id;

uniform mat4 mvp;
uniform vec3 player_pos;
uniform float player_yaw;
uniform float player_pitch;
uniform float right_arm_angle;
uniform float right_arm_z_angle;
uniform float left_arm_angle;
uniform float left_arm_z_angle;
uniform float right_leg_angle;
uniform float left_leg_angle;
uniform float _hidehead;
uniform float headyawoff;
uniform float crouch;

out vec2 v_uv;
out vec3 v_normal;
out vec3 v_world_pos;

void main() {
    float LEG_H   = 0.75;
    float BODY_H  = 0.75;
    float HEAD_SIZE = 0.5;
    float BODY_HW = 0.25;
    float ARM_HW  = 0.125;
    float ARM_OX  = BODY_HW + ARM_HW;
    float LEG_HW  = 0.125;
    float NECK_Y  = LEG_H + BODY_H;

    vec3 pos  = in_pos;
    vec3 norm = in_norm;

    int  pid = int(in_part_id + 0.5);
    bool hd  = (pid == 1);
    bool ra  = (pid == 2);
    bool la  = (pid == 3);
    bool rl  = (pid == 4);
    bool ll  = (pid == 5);

    float sdy = LEG_H + BODY_H;
    float hy  = LEG_H;

    // R_x(arm) then R_z(zswing) @ shoulder pivot
    if (ra) {
        vec3 piv = vec3(ARM_OX, sdy, 0.0);
        vec3 rel = pos - piv;
        float a = radians(right_arm_angle);
        float c = cos(a), s = sin(a);
        rel    = vec3(rel.x, rel.y*c - rel.z*s, rel.y*s + rel.z*c);
        norm = vec3(norm.x, norm.y*c - norm.z*s, norm.y*s + norm.z*c);
        float za = radians(right_arm_z_angle);
        float cz = cos(za), sz = sin(za);
        rel    = vec3(rel.x*cz - rel.y*sz, rel.x*sz + rel.y*cz, rel.z);
        norm = vec3(norm.x*cz - norm.y*sz, norm.x*sz + norm.y*cz, norm.z);
        pos = rel + piv;
    } else if (la) {
        vec3 piv = vec3(-ARM_OX, sdy, 0.0);
        vec3 rel = pos - piv;
        float a = radians(left_arm_angle);
        float c = cos(a), s = sin(a);
        rel    = vec3(rel.x, rel.y*c - rel.z*s, rel.y*s + rel.z*c);
        norm = vec3(norm.x, norm.y*c - norm.z*s, norm.y*s + norm.z*c);
        float za = radians(left_arm_z_angle);
        float cz = cos(za), sz = sin(za);
        rel    = vec3(rel.x*cz - rel.y*sz, rel.x*sz + rel.y*cz, rel.z);
        norm = vec3(norm.x*cz - norm.y*sz, norm.x*sz + norm.y*cz, norm.z);
        pos = rel + piv;
    } else if (rl) {
        // R_x(leg) @ hip
        float a = radians(right_leg_angle);
        float c = cos(a), s = sin(a);
        vec3 piv = vec3(LEG_HW, hy, 0.0);
        vec3 rel = pos - piv;
        pos    = vec3(rel.x, rel.y*c - rel.z*s, rel.y*s + rel.z*c) + piv;
        norm = vec3(norm.x, norm.y*c - norm.z*s, norm.y*s + norm.z*c);
    } else if (ll) {
        float a = radians(-left_leg_angle);
        float c = cos(a), s = sin(a);
        vec3 piv = vec3(-LEG_HW, hy, 0.0);
        vec3 rel = pos - piv;
        pos    = vec3(rel.x, rel.y*c - rel.z*s, rel.y*s + rel.z*c) + piv;
        norm = vec3(norm.x, norm.y*c - norm.z*s, norm.y*s + norm.z*c);
    }

    // head: R_x(pitch) R_y(yawoff) @ neck
    if (hd) {
        vec3 neck = vec3(0.0, NECK_Y, 0.0);
        vec3 rel  = pos - neck;
        float pr  = radians(-player_pitch);
        float cp = cos(pr), sp = sin(pr);
        rel    = vec3(rel.x, rel.y*cp - rel.z*sp, rel.y*sp + rel.z*cp);
        norm = vec3(norm.x, norm.y*cp - norm.z*sp, norm.y*sp + norm.z*cp);
        float hyo = radians(headyawoff);
        float chy = cos(hyo), shy = sin(hyo);
        rel    = vec3(rel.x*chy - rel.z*shy, rel.y, rel.x*shy + rel.z*chy);
        norm = vec3(norm.x*chy - norm.z*shy, norm.y, norm.x*shy + norm.z*chy);
        pos = rel + neck;
    }

    // R_x(crouch*0.5) @ hip for upper body tilt
    if (crouch > 0.01) {
        float ca = crouch * 0.5;
        float cc = cos(ca), sc = sin(ca);
        if (!rl && !ll) {
            vec3 hip  = vec3(0.0, hy, 0.0);
            vec3 crel = pos - hip;
            pos    = vec3(crel.x, crel.y*cc - crel.z*sc, crel.y*sc + crel.z*cc) + hip;
            norm = vec3(norm.x, norm.y*cc - norm.z*sc, norm.y*sc + norm.z*cc);
        }
        if (rl || ll) pos.z += crouch * 0.1;
    }

    // R_y(yaw - 90) -> world space
    float yr = radians(player_yaw - 90.0);
    float cy = cos(yr), sy = sin(yr);

    vec3 rpos  = vec3(pos.x*cy - pos.z*sy, pos.y, pos.x*sy + pos.z*cy);
    vec3 rnorm = vec3(norm.x*cy - norm.z*sy, norm.y, norm.x*sy + norm.z*cy);

    v_normal = rnorm;

    // float head_scale = 1.0;

    if (_hidehead > 0.5 && hd) {
        gl_Position = vec4(0.0, 0.0, -10.0, 1.0);
        v_uv        = in_uv;
        v_world_pos = vec3(0.0);
    } else {
        vec3 wp     = rpos + player_pos;
        gl_Position = mvp * vec4(wp, 1.0);
        v_uv        = in_uv;
        v_world_pos = wp;
    }
}
