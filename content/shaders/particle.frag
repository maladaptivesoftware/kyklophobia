#version 330
uniform sampler2D texture0;

in vec2 v_uv;
in float v_alpha;
in vec3 v_tint;

out vec4 f_color;

void main() {
    vec4 tex = texture(texture0, v_uv);
    if (tex.a < 0.1) discard;
    f_color = vec4(tex.rgb * v_tint, tex.a * v_alpha);
}
