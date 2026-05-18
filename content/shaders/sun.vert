#version 330
in vec2 in_offset;
uniform mat4 mvp;
uniform vec3 sun_pos;
uniform vec3 cam_r;
uniform vec3 cam_u;
uniform float sun_sz;
out vec2 v_offset;
void main() {
    v_offset = in_offset;
    vec3 world_pos = sun_pos + (cam_r * in_offset.x + cam_u * in_offset.y) * sun_sz;
    gl_Position = mvp * vec4(world_pos, 1.0);
}
