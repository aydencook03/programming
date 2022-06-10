// TODO / Ideas:
// - add ability for constraints to break
//       - should work in static & in force constraints
//       - add breaking distance (0 if none)
//       - in match statement, if over distance -> broken = true
//       - add broken bool
//       - in match statement, remove constraint if bool = true
// - make completely standalone
//       - no draw code, so that rendering can be done independently. ie, render a solid rigid/soft body, fluid, etc
//       - implement a rendering plugin api?
//             - send a packet of particle coordinates+radii & constraints/forces to be drawn?
//       - this can be used to allow for both real-time and baked rendering
// - viscosity how? want this "engine" to be general enough for fluid sim?
// - youtube playlist for ideas: https://youtube.com/playlist?list=PLvypLlLlZuNhcdtPKfQ25cpmhBuWWDZzR
// - convert to lib crate type, and make it a git submodule
// - take a snapshot of a simulation. save it in a file. load from a file.
// - web canvas frontend

struct Sim {
    updates_per_sec: u8,
    constraint_passes: u8,
    particles: Vec<Particle>,
    static_constraints: Vec<Constraint>,
    forces: Vec<Force>,
}

impl Sim {
    fn new() -> Sim {
        Sim {
            updates_per_sec: 60,
            constraint_passes: 3,
            ..Default::default()
        }
    }

    fn handle_static_constraints(self: &Self) {
        for _ in 0..self.constraint_passes {
            for constraint in self.static_constraints {
                constraint.handle_statically();
            }
        }
    }

    fn send_forces_to_particles(self: &mut Self) {
        for force in self.forces {
            force.send_force();
        }
    }

    fn add_particle(self: &mut Self) {
        todo!();
    }

    fn add_body(self: &mut Self, type: Body) {
        todo!();
    }

    fn run(self: &Self) {
        todo!();
    }
}

/// Constraint on a Particle or between linked Particles.
/// This simply holds the data, and can be used as a static constraint or a constraint force elsewhere
enum Constraint {
    /// Pin a Particle to a point
    PinToPoint { particle: &mut Particle, point: Vec2 },
    // BoundaryLine { particle: &mut Particle, start: Vec2, end: Vec2 },
    // InsidePolygon { particle: &mut Particle, points: Vec<Vec2> },
    /// Keep a Particle outside of a polygon
    OutsidePolygon { particle: &mut Particle, points: Vec<Vec2> },
    FixedDistance { particle: &mut Particle, point: Vec2, dist: f64 },
    MinDistance { particle: &mut Particle, point: Vec2, dist: f64 },
    MaxDistance { particle: &mut Particle, point: Vec2, dist: f64 },

    LinkFixedDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
    LinkMinDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
    LinkMaxDistance { particle1: &mut Particle, particle2: &mut Particle, dist: f64 },
}

impl Constraint {
    /// Handle the Constraint statically
    fn handle_statically(self: &Self) {
        todo!();
    }
}

/// Force on a Particle or between interacting Particles
enum Force {
    /// A raw 2d force
    Raw { particle: &mut Particle, force: Vec2 },

    /// A general restoring force (F = -kx^n - bv) that attempts to satisfy a given constraint. Ex:
    /// - gravity {(Link)MaxDistance, G*mass*mass, -2, 0}
    /// - dampened spring between Particles {LinkFixedDistance, stiffness, 1, 0.5}
    /// - stiff pendulum {FixedDistance, 99, 1, 99}
    ConstraintForce { constraint_type: Constraint, k: f64, n: f64, b: f64 },

    /// A simple downwards pull of gravity (F = -mg)
    WorldGravity { particle: &mut Particle, g: f64 },

    /// Newtonian gravitational attraction between two Particles
    Gravity { particle1: &mut Particle, particle2: &mut Particle },
}

impl Force {
    /// Send the Force to the Particle(s)
    fn send_force(self: &Self) {
        todo!();
    }
}