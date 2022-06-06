/// A 2d euclidean vector
struct Vector {
    x: f64,
    y: f64
}

impl Vector {
    /// Constructor function: returns a 0 Vector
    fn new() -> Vector {
        Vector {
            x: 0.0,
            y: 0.0
        }
    }
}

enum Constraint {
    PinToPoint(Vector),
    BoundaryLine(Vector, Vector),
    RigidRod(Vector),
    RigidRodLink(&Body),
    ChainLink(&Body)
}

struct Body {
    mass: f64,
    radius: f64,
    color: Color,
    pos: Vector,
    vel: Vector,
    accel: Vector,

    constraints: Vec<Constraint>,
    forces: Vec<Vector>
}

impl Body {
    /// Constructor function
    fn new() -> Body {
        Body {
            mass: 10.0,
            radius: 10.0,
            //color: CRIMSON,
            pos: Vector::new(),
            vel: Vector::new(),
            accel: Vector::new(),

            constraints: Vec::new(),
            forces: Vec::new()
        }
    }

    fn handle_constraints(self: &mut Self) {
        for constraint in self.constraints {
            match constraint {

            }
        }
    }

    fn handle_forces(self: &mut Self) {
        self.accel.x = 0.0;
        self.accel.y = 0.0;

        for force in self.forces {
            self.accel.x += force.x / self.mass;
            self.accel.y += force.y / self.mass;
        }
    }

    /// A first-order symplectic integrator
    fn symplectic_euler_update(self: &mut Self, dt: f64) {
        self.vel.x += self.accel.x * dt;
        self.vel.y += self.accel.y * dt;
        self.pos.x += self.vel.x * dt;
        self.pos.y += self.vel.y * dt;
    }

    /// A second-order symplectic integrator
    fn verlet_update(self: &mut Self, dt: f64) {

    }
}