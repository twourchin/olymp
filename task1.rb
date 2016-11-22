N = readlines[0].to_i

def own_numbers n
  arr = []
  loop do
    arr.push n%10
    break arr if (n=n/10) == 0
  end
end

def div_by_own_numbers_sum? n
  return true if ( n % own_numbers(n).reduce(:+) ) == 0
end

count = 0
for i in 1..N
  count+=1 if div_by_own_numbers_sum? i
end

puts count
