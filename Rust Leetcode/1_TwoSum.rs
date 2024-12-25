use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&prev_index) = map.get(&complement) {
                return vec![prev_index as i32, i as i32];
            }
            map.insert(num, i);
        }
        
        vec![-1, -1] // Return [-1, -1] if no solution found
    }
}