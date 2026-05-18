#version 330
in vec2 in_offset;
in vec2 in_uv;

uniform mat4 mvp;
uniform vec3 center_pos;
uniform vec3 cam_r;
uniform vec3 cam_u;
uniform vec2 size;

out vec2 v_uv;

void main() {
    v_uv = in_uv;
    vec3 world_pos = center_pos + (cam_r * in_offset.x * size.x) + (cam_u * in_offset.y * size.y);
    gl_Position = mvp * vec4(world_pos, 1.0);
}
