from ex_9_7_vector2d_v4 import Vector2d_v4


class Vector2d_v5(Vector2d_v4):
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
