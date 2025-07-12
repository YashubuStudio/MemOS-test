from my_cube import MyCube


def test_default_init(tmp_path):
    cube = MyCube()
    assert cube.text_mem == []
    assert cube.act_mem == []
    assert cube.para_mem == []

    cube.text_mem.append("a")
    cube.dump(tmp_path)
    cube.text_mem.clear()
    cube.load(tmp_path)
    assert cube.text_mem == ["a"]
