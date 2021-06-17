from core import core


def test():
    output = core.get_container_output(
        core.start_container("alpine", commands=["echo hello stage"], port={f'8080/tcp': 8080}, daemon=True))

    print(output)
