#version 330

uniform sampler2D DiffuseSampler;
uniform float gamma;

in vec2 texCoord;
out vec4 fragColor;

void main() {
    vec4 dc  = texture(DiffuseSampler, texCoord);
    vec3 woc = pow(dc.rgb, vec3(1.0/gamma));  // rgb^(1/γ)
    fragColor = vec4(woc, 1.0);
}
