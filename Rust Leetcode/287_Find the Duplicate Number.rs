impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut slow = nums[0];
        let mut fast = nums[nums[0] as usize];

        while slow != fast {
            slow = nums[slow as usize];
            fast = nums[nums[fast as usize] as usize];
        }

        let mut slow2 = 0;
        while slow2 != slow {
            slow = nums[slow as usize];
            slow2 = nums[slow2 as usize];
        }

        slow
    }
}
