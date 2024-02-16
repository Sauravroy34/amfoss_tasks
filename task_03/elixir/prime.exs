defmodule Prime do

  def check(number) do
      if number == 2 do
          true
      else
          Enum.all?(2..(number-1), &rem(number,&1) != 0)

      end
  end



  def give(n), do:  Enum.filter(1..n,&check(&1))



end

number_str = IO.gets("Enter a number: ")
number = String.trim(number_str) |> String.to_integer()


IO.inspect Prime.give(number)
