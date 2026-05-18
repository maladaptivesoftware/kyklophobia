#version 330
uniform sampler2D hud_texture;
in vec2 v_uv;
out vec4 f_color;
void main() {
    vec4 color = texture(hud_texture, v_uv);
    if (color.a < 0.1) discard;
    f_color = vec4(color.rgb * 0.7, color.a);
}
