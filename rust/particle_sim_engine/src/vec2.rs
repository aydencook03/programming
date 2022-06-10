/// A 2d euclidean vector
#[derive(Copy, Clone, Default)]
struct Vec2d {
    x: f64,
    y: f64,
}

impl Vec2d {
    /// Constructor function: returns a zero Vec2d (using Default for f64)
    fn new() -> Vec2d {
        Vec2d { ..Default::default() }
    }

    /// Returns the magnitude of the Vec2d
    fn mag(self: &Self) -> f64 {
        (self.x*self.x + self.y*self.y).powf(0.5_f64)
    }
}