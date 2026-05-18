#version 330
in vec3 in_pos;
in vec2 in_uv;
in vec3 in_norm;
in float in_part_id;

uniform mat4 mvp;
uniform float model_yaw;
uniform float model_pitch;
uniform float model_scale;

out vec2 v_uv;
out vec3 v_normal;

void main() {
    float LEG_H  = 0.75;
    float BODY_H = 0.75;
    float HEAD_SIZE = 0.5;
    float NECK_Y = LEG_H + BODY_H;
    float MDL_H  = LEG_H + BODY_H + HEAD_SIZE;

    vec3 pos  = in_pos;
    vec3 norm = in_norm;

    int  pid = int(in_part_id + 0.5);

    float yr = radians(model_yaw);
    float cy = cos(yr), sy = sin(yr);

    vec3 rpos, rnorm;

    // head: R_x(pitch) @ neck, then R_y(yaw) with body
    if (pid == 1) {
        vec3 neck = vec3(0.0, NECK_Y, 0.0);
        vec3 rel  = pos - neck;
        float pr  = radians(model_pitch);
        float cp = cos(pr), sp = sin(pr);
        vec3 pp = vec3(rel.x, rel.y*cp - rel.z*sp, rel.y*sp + rel.z*cp);
        vec3 pn = vec3(norm.x, norm.y*cp - norm.z*sp, norm.y*sp + norm.z*cp);
        rpos  = vec3(pp.x*cy - pp.z*sy, pp.y, pp.x*sy + pp.z*cy) + neck;
        rnorm = vec3(pn.x*cy - pn.z*sy, pn.y, pn.x*sy + pn.z*cy);
    } else {
        rpos  = vec3(pos.x*cy - pos.z*sy, pos.y, pos.x*sy + pos.z*cy);
        rnorm = vec3(norm.x*cy - norm.z*sy, norm.y, norm.x*sy + norm.z*cy);
    }

    /*
    rpos -= vec3(0.0, MDL_H * 0.5, 0.0);
    rpos  = rpos * model_scale;
    */
    // center @ MDL_H/2 then scale to fit viewport
    rpos.y -= MDL_H / 2.0;
    rpos   *= model_scale;

    v_normal    = rnorm;
    v_uv        = in_uv;
    gl_Position = mvp * vec4(rpos, 1.0);
}
