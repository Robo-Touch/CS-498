import pygmsh

def main(width, length, height):
    with pygmsh.occ.Geometry() as geom:
        sketch = geom.add_rectangle(
            [0.0, 0.0, 0.0],  # lower-left corner
            width,
            length
        )
        geom.extrude(sketch, [0.0, 0.0, height])
        mesh = geom.generate_mesh()

    return mesh

if __name__ == '__main__':
    mesh = main(width=50, length=60, height=10.0)
    mesh.write('box.stl')
