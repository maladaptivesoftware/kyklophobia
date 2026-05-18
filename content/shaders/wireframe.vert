#version 330
in vec3 in_pos;
uniform mat4 mvp;
uniform vec3 offset;
void main() {
    gl_Position = mvp * vec4(in_pos + offset, 1.0);
}
