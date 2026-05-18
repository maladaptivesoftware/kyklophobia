#version 330

in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;

uniform mat4 mvp;
uniform vec3 item_pos;
uniform float rotation;
uniform float bob_offset;
uniform float scale;
uniform vec3 tint;
uniform int tint_mode;

out vec2 v_uv;
out vec3 v_normal;
out vec3 v_frag_pos;
out vec3 v_tint;

void main() {
    // R_y(rotation) spin, scaled
    float c = cos(rotation), s = sin(rotation);
    mat3 ry = mat3(c, 0, s, 0, 1, 0, -s, 0, c);

    vec3 rp = ry * (in_pos * scale);
    vec3 wp = rp + item_pos + vec3(0.0, bob_offset, 0.0);

    gl_Position = mvp * vec4(wp, 1.0);
    v_uv      = in_uv;
    v_normal  = ry * in_norm;
    v_frag_pos = wp;
    v_tint = tint_mode == 1 ? (in_norm.y > 0.9 ? tint : vec3(1.0)) : tint;
}
