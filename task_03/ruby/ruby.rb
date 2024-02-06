def is_prime(num)
    return false if num <= 1
    
    (2..num).each do |i|
        return false if num % i == 0
    end
    
    true
end

puts "Enter a number (n): "
n = gets.chomp.to_i

puts "Prime numbers up to #{n}:"
(2..n).each do |i|
    puts i if is_prime(i)
end


