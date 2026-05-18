#version 330
in vec3 in_pos;
in vec3 in_norm;
in float in_ao;
in vec2 in_uv;
uniform mat4 mvp;
out vec3 v_normal;
out float v_ao;
out vec2 v_uv;
out float v_height;
out vec3 v_world_pos;
void main() {
    gl_Position = mvp * vec4(in_pos, 1.0);
    v_normal = in_norm;
    v_ao = in_ao;
    v_uv = in_uv;
    v_height = in_pos.y;
    v_world_pos = in_pos;
}
