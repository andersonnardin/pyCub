"""Test pyCub skin sensors using the optional PyBullet GUI."""

from icub_pybullet.pycub import pyCub


def main() -> None:
    client = pyCub(config="skin_test_pybullet_gui.yaml")

    while client.is_alive():
        client.update_simulation(None)


if __name__ == "__main__":
    main()
