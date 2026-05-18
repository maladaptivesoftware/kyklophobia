#version 330

in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;

uniform mat4 mvp;
uniform vec3 player_pos;
uniform float byaw;
uniform float arm_angle;
uniform float arm_z_angle;
uniform float crouch;
uniform float scale;
uniform vec3 hand_offset;
uniform float item_yaw;
uniform float item_pitch;
uniform float item_roll;
uniform vec3 tint;
uniform int tint_mode;

out vec2 v_uv;
out vec3 v_normal;
out vec3 v_frag_pos;
out vec3 v_tint;

// col-major 3x3 rotation matrices
mat3 rx(float a) {
    float c = cos(a), s = sin(a);
    return mat3(1,0,0, 0,c,s, 0,-s,c);
}
mat3 ry(float a) {
    float c = cos(a), s = sin(a);
    return mat3(c,0,s, 0,1,0, -s,0,c);
}
mat3 rz(float a) {
    float c = cos(a), s = sin(a);
    return mat3(c,s,0, -s,c,0, 0,0,1);
}

void main() {
    float ARM_OX     = 0.375;
    float LEG_H      = 0.75;
    float BODY_H     = 0.75;
    float shoulder_y = LEG_H + BODY_H;
    float hip_y      = LEG_H;

    // item = R_y(yaw) * R_x(pitch) * R_z(roll) * (p * scale)
    mat3 ir  = ry(item_yaw) * rx(item_pitch) * rz(item_roll);
    vec3 pos  = ir * (in_pos * scale);
    vec3 norm = ir * in_norm;

    pos += hand_offset;

    // R_x(arm) R_z(zswing) @ shoulder pivot
    mat3 arx = rx(radians(arm_angle));
    pos = arx * pos;  norm = arx * norm;

    mat3 arz = rz(radians(arm_z_angle));
    pos = arz * pos;  norm = arz * norm;

    pos += vec3(-ARM_OX, shoulder_y, 0.0);

    if (crouch > 0.01) {
        mat3 cr  = rx(crouch * 0.5);
        vec3 hip = vec3(0.0, hip_y, 0.0);
        pos  = cr * (pos - hip) + hip;
        norm = cr * norm;
    }

    mat3 yr = ry(radians(byaw - 90.0));
    pos  = yr * pos;
    norm = yr * norm;

    vec3 wp = pos + player_pos;
    gl_Position = mvp * vec4(wp, 1.0);
    v_uv       = in_uv;
    v_normal   = norm;
    v_frag_pos = wp;
    v_tint     = tint_mode == 1 ? (in_norm.y > 0.9 ? tint : vec3(1.0)) : tint;
}
