#version 330
uniform sampler2D ui_texture;
in vec2 v_uv;
out vec4 f_color;
void main() {
    vec4 color = texture(ui_texture, v_uv);
    if (color.a < 0.1) discard;
    f_color = vec4(color.rgb * 0.8, color.a);
}
