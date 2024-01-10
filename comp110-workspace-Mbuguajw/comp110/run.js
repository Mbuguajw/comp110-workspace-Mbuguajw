function MaxSubvector2(A) {
    var num_sums_executed = 0;
    var maxsum = 0;
    var n = len(A);
    for (var i=0; i<n; i++) {
        for (var j=0; j<n; i++) {
            var sum = 0;
            for (var k=i; k<j+1; k++) {
                num_sums_executed += 1;
                sum = sum + A[k];
            }
            maxsum = max(sum, maxsum);
        }
    }
    print ('Array size=', n, ' maxsum=', maxsum, 'num_sums_executed=', num_sums_executed);
    return [maxsum, num_sums_executed]
}

function FIND_MAXIMUM_SUBARRAY(A, low, high) {​​
    if (high==low) {
        return [low, high, A[low], 0];
    }​​
    else {
        var mid = floor((low + high)/2);​​
        var num_sums_executed;​
        var num_sum_left;​​
        var num_sum_right;​​
        var num_sum_cross;​​
        var right_low;​​
        var right_high;​​
        var right_sum;​​
        var left_low;​​
        var left_high;​​
        var left_sum;
        var cross_low;
        var cross_high;
        var cross_sum;
        var mid = floor((low + high)/2);
        [left_low, left_high, left_sum, num_sum_left] = FIND_MAXIMUM_SUBARRAY(A, low, mid);​
        [right_low, right_high, right_sum, num_sum_right] = FIND_MAXIMUM_SUBARRAY(A, mid + 1, high);​​
        [cross_low, cross_high, cross_sum, num_sum_cross] = FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high);​​
        num_sums_executed = num_sum_left + num_sum_right + num_sum_cross;​​
        if (left_sum >= right_sum && left_sum >= cross_sum) {​​
            return [left_low, left_high, left_sum, num_sums_executed ];​​
        }
        else if (right_sum >= left_sum && right_sum >= cross_sum) {​​
            return [right_low, right_high, right_sum, num_sums_executed ];​​
        }​​
        else {​​
            return [cross_low, cross_high, cross_sum, num_sums_executed ];​​
        }
    }
}
// [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]​​
print(FIND_MAXIMUM_SUBARRAY([1], 1, 1))