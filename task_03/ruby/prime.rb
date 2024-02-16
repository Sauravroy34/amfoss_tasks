def check(n)
  if n == 2
    return true
  end

  for i in 2..n-1 do
    if n % i == 0
      return false
    end
  end

  return true
end

puts "enter a number"
number = gets.chomp.to_i

if number < 2
  puts "prime number not defined"




else
  for j in 2..number do
    if check(j)
      puts "prime number is #{j}"

    end
  end
end
