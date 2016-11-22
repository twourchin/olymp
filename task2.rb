class Pair
  attr_reader :diff

  def initialize(index, score)
    @score = score
    @index = index
    @diff = @score[@index+1]-@score[@index]
  end

  def <=> value
    @diff <=> value.diff
  end

  def bonus
    @score[@index+1]*2
  end

  def exclude!
    @score.fill 0, @index, 2
  end

  def excluded?
    @score[@index]==0 || @score[@index+1]==0
  end

end

score = readlines.join(' ').split(' ').map { |value| value.to_i }

pairs=[]
for i in 0...score.count-1 do
  pairs.push Pair.new(i, score)
end

pairs.sort!.reverse!

bonus_sum = 0
pairs.each do |pair|
  next if pair.excluded?
  break if pair.diff < 1

  bonus_sum = bonus_sum + pair.bonus
  pair.exclude!
end

puts bonus_sum + score.reduce(:+)

