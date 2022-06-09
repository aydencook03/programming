struct Sim {
    physics_fps: u8,
    draw_fps: u8,
    constraint_passes: u8,
    particles: Vec<Particle>,
    static_constraints: Vec<Constraint>,
    forces: Vec<Force>,
}

impl Sim {
    fn new() -> Sim {
        Sim {
            physics_fps: 60,
            draw_fps: 60,
            constraint_passes: 3,
            ..Default::default()
        }
    }

    fn handle_static_constraints(self: &Self) {
        for _ in 0..self.constraint_passes {
            for constraint in self.static_constraints {
                match constraint {
                    _ => println!("Not Implemented"),
                }
            }
        }
    }

    fn send_forces_to_particles(self: &mut Self) {
        todo!();
    }

    fn add_particle(self: &mut Self) {
        todo!();
    }

    fn add_body(self: &mut Self, type: Body) {
        todo!();
    }
}

/// Constraint on a Particle or between linked Particles
enum Constraint {
    PinToPoint { particle: &mut Particle, point: Vec2d },
    Polygon { points: Vec<Vec2d> },
    FixedDistance { particle: &mut Particle, point: Vec2d, dist: f64 },
    MinDistance { particle: &mut Particle, point: Vec2d, dist: f64 },
    MaxDistance { particle: &mut Particle, point: Vec2d, dist: f64 },

    LinkFixedDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
    LinkMinDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
    LinkMaxDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
}

/// Force on a Particle or between interacting Particles
enum Force {
    /// A raw 2d force
    Raw { particle: &mut Particle, force: Vec2d },

    /// A general restoring force (F=-kx^n) that attempts to satisfy a given constraint. Ex:
    /// - gravity {(Link)MaxDistance, G*mass*mass, -2}
    /// - spring between Particles
    /// - stiff pendulum
    ConstraintForce { constraint_type: Constraint, k: f64, n: f64 },

    /// Gravitational attraction between two Particles
    Gravity { particle1: &mut Particle, particle2: &mut Particle },
}