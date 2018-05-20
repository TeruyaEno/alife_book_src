import numpy as np
from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;
    attribute vec2 texcoord;
    varying vec2 v_texcoord;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
        v_texcoord = texcoord;
    }
"""

fragment = """
    uniform sampler2D texture;
    varying vec2 v_texcoord;
    void main()
    {
        float r = texture2D(texture, v_texcoord).r;
        gl_FragColor = vec4(r,r,r,1);
    }
"""

window = app.Window(width=512, height=512)

@window.event
def on_draw(dt):
    quad['texture'] = (np.random.rand(20,10) * 256).astype(np.uint8)
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)



quad = gloo.Program(vertex, fragment, count=4)
quad['position'] = [(-1,-1), (-1,+1), (+1,-1), (+1,+1)]
quad['texcoord'] = [( 0, 1), ( 0, 0), ( 1, 1), ( 1, 0)]
quad['texture'] = (np.random.rand(20,10) * 256).astype(np.uint8)
app.run()

print("test")
