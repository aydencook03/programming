/// A physical particle.  Is only aware of its own properties, state, and the forces acting on it (obeys locality)
#[derive(Default)]
struct Particle {
    mass: f64,
    charge: f64,
    radius: f64,
    color: (u8, u8, u8),
    pos: Vec2d,
    prev_pos: Vec2d,
    vel: Vec2d,
    accel: Vec2d,

    forces: Vec<Vec2d>,
}

impl Particle {
    /// Constructor function
    fn new() -> Particle {
        Particle {
            mass: 10.0,
            radius: 10.0,
            color: (220, 20, 60), //CRIMSON,
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

    /// A first-order symplectic integrator (Semi-implicic/Symplectic Euler)
    fn symplectic_euler_update(self: &mut Self, dt: f64) {
        self.vel.x += self.accel.x * dt;
        self.vel.y += self.accel.y * dt;
        self.pos.x += self.vel.x * dt;
        self.pos.y += self.vel.y * dt;

        self.prev_pos.x = self.pos.x;
        self.prev_pos.y = self.pos.y;
    }

    /// A second-order symplectic integrator (Basic Störmer–Verlet)
    fn verlet_update(self: &mut Self, dt: f64) {
        if self.vel.mag() != 0.0 {
            self.pos.x = self.pos.x + self.vel.x*dt + 0.5*self.accel.x*dt*dt;
            self.pos.y = self.pos.y + self.vel.y*dt + 0.5*self.accel.y*dt*dt;

            self.vel.x = 0.0;
            self.vel.y = 0.0;
        } else {
            self.pos.x = 2*self.pos.x - self.prev_pos.x + self.accel.x*dt*dt;
            self.pos.y = 2*self.pos.y - self.prev_pos.y + self.accel.y*dt*dt;
        }

        self.prev_pos.x = self.pos.x;
        self.prev_pos.y = self.pos.y;
    }
}