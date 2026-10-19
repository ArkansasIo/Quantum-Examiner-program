use num_complex::Complex64;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub struct BlochVector { pub x:f64, pub y:f64, pub z:f64 }
impl BlochVector {
    pub fn radius(&self)->f64 {(self.x*self.x+self.y*self.y+self.z*self.z).sqrt()}
    pub fn physical(&self,eps:f64)->bool {self.radius()<=1.0+eps}
}

#[derive(Debug, Clone, Copy)]
pub struct Qubit {pub alpha:Complex64,pub beta:Complex64}
impl Qubit {
    pub fn zero()->Self {Self{alpha:Complex64::new(1.0,0.0),beta:Complex64::new(0.0,0.0)}}
    pub fn normalize(&mut self){let n=(self.alpha.norm_sqr()+self.beta.norm_sqr()).sqrt();if n==0.0{panic!("zero state")};self.alpha/=n;self.beta/=n;}
    pub fn bloch(&mut self)->BlochVector {self.normalize();let c=self.alpha.conj()*self.beta;BlochVector{x:2.0*c.re,y:2.0*c.im,z:self.alpha.norm_sqr()-self.beta.norm_sqr()}}
}
