"""Push the ball with joint control using the optional PyBullet GUI."""

from icub_pybullet.examples.push_the_ball_pure_joints import push_the_ball
from icub_pybullet.pycub import pyCub


def main() -> None:
    client = pyCub(config="with_ball_pybullet_gui.yaml")
    push_the_ball(client)

    while client.is_alive():
        client.update_simulation()


if __name__ == "__main__":
    main()
