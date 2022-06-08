/// A 2d euclidean vector
struct Vector2 {
    x: f64,
    y: f64,
}

impl Vector2 {
    /// Constructor function: returns a zero Vector2
    fn new() -> Vector2 {
        Vector2 {
            x: 0.0,
            y: 0.0,
        }
    }

    /// Returns the magnitude of the Vector2
    fn mag(self: &Self) -> f64 {
        (self.x.powi(2_i32) + self.y.powi(2_i32)).powf(0.5_f64)
    }
}