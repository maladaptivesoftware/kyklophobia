#version 330

in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;

uniform mat4 mvp;
uniform vec3 world_pos;
uniform vec3 tint;

out vec2 v_uv;
out vec3 v_normal;
out vec3 v_tint;

void main() {
    gl_Position = mvp * vec4(in_pos + world_pos, 1.0);
    v_uv = in_uv;
    v_normal = in_norm;
    v_tint = tint;
}
