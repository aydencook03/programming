/// A physical particle.  Is only aware of its own properties, state, and the forces acting on it (obeys locality)
#[derive(Default)]
struct Particle {
    mass: f64,
    charge: f64,
    radius: f64,
    color: (u8, u8, u8),
    pos: Vec2,
    vel: Vec2,
    accel: Vec2,
    forces: Vec<Vec2>,
}

impl Particle {
    /// Constructor function
    fn new() -> Particle {
        Particle {
            mass: 10.0,
            radius: 10.0,
            color: (220, 20, 60, 1), //CRIMSON,
            ..Default::default()
        }
    }

    /// Adds up all of the forces on the Particle
    fn sum_forces(self: &mut Self) {
        self.accel.x = 0.0;
        self.accel.y = 0.0;

        for force in self.forces {
            self.accel.x += force.x / self.mass;
            self.accel.y += force.y / self.mass;
        }
    }

    /// A first-order symplectic integrator that updates the Particle (uses Semi-implicic/Symplectic Euler)
    fn symplectic_euler_update(self: &mut Self, dt: f64) {
        self.vel.x += self.accel.x * dt;
        self.vel.y += self.accel.y * dt;
        self.pos.x += self.vel.x * dt;
        self.pos.y += self.vel.y * dt;
    }

    /// A second-order symplectic integrator that updates the Particle (uses Basic Störmer–Verlet)
    fn verlet_update(self: &mut Self, dt: f64) {
        todo!();
    }
}