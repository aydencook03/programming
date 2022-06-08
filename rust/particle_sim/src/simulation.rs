/// Static constraints on a Particle or between linked Particles
enum StaticConstraint {
    PinToPoint { particle: &mut Particle, point: Vector2 },
    BoundaryLine { particle: &mut Particle, start: Vector2, end: Vector2 },
    FixedDistance { particle: &mut Particle, point: Vector2, dist: f64 },
    MinDistance { particle: &mut Particle, point: Vector2, dist: f64 },
    MaxDistance { particle: &mut Particle, point: Vector2, dist: f64 },

    LinkFixedDistance { first_particle: &mut Particle, second_particle: &mut Particle dist: f64 },
    LinkMinDistance { first_particle: &mut Particle, second_particle: &mut Particle dist: f64 },
    LinkMaxDistance { first_particle: &mut Particle, second_particle: &mut Particle dist: f64 },
}

// What about constraint forces? think...
enum ConstraintForce {
    Collide,
    Normal,
    Spring,
    Gravity,
}

struct Sim {
    physics_fps: u8,
    draw_fps: u8,
    constraint_passes: u8,
    particles: Vec<Particle>,
    constraints: Vec<StaticConstraint>,
}

impl Sim {
    fn handle_static_constraints(self: &Self) {
        for _ in 0..self.constraint_passes {
            for constraint in self.static_constraints {
                match constraint {
                    _ => println!("Not Implemented"),
                }
            }
        }
    }

    fn push_particle(self: &mut Self) {
        todo!();
    }

    fn push_body(self: &mut Self, type: Body) {
        todo!();
    }
}