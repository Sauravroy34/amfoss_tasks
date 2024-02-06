defmodule PrimeNumbers do
  def is_prime?(num) when num <= 1, do: false
  def is_prime?(num) do
    Enum.all?(2..div(num, 2), fn x -> rem(num, x) != 0 end)
  end

  def prime_numbers_up_to(n) do
    Enum.filter(2..n, &is_prime?/1)
  end

  def main do
    IO.puts("Enter a number (n):")
    n = String.to_integer(IO.gets(""))

    IO.puts("Prime numbers up to #{n}:")
    prime_numbers = prime_numbers_up_to(n)
    Enum.each(prime_numbers, fn prime -> IO.write("#{prime} ") end)
    IO.puts("")
  end
end

PrimeNumbers.main()

