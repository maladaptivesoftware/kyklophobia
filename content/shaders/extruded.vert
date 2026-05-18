#version 330
in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;
in vec3 instance_pos;
out vec2 uv;
out vec3 normal;
uniform mat4 mvp;
uniform vec3 tint;
void main() {
    vec3 pos = in_pos + instance_pos;
    gl_Position = mvp * vec4(pos, 1.0);
    uv = in_uv;
    normal = in_norm;
}
