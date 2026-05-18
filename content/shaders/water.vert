#version 330
in vec2 in_pos;
uniform mat4 mvp;
uniform vec3 camera_pos;
uniform float water_level;
out vec3 v_world_pos;
out vec4 v_clip_pos;
void main() {
    vec3 world_pos = vec3(camera_pos.x + in_pos.x, water_level, camera_pos.z + in_pos.y);
    gl_Position = mvp * vec4(world_pos, 1.0);
    v_world_pos = world_pos;
    v_clip_pos = gl_Position;
}
