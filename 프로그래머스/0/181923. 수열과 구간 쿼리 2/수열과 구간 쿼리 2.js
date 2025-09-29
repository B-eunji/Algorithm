function solution(arr, queries) {
    let results = [];
    
    for(let [s,e,k] of queries){
        let min = Infinity;
        for(let i = s; i < e+1; i++){
            if (arr[i] > k){
                min = Math.min(min, arr[i])
            }
        }
        results.push(min === Infinity ? -1 : min);
    }
    return results;
}