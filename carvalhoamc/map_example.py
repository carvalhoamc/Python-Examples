# Copyright (C) <2018>  <Alexandre Miguel de Carvalho>
#                       <https://www.linkedin.com/in/carvalhoamc/>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#



import numpy as np

base = np.array([10, 20, 30, 40, 50])
exponents = np.array([2, 2, 2, 2, 2])
varing_exponents = np.array([1,2,3,4,5])

#Here, we use map and lambda
square_of_array = map(lambda n: n**2,base)
print("Using map() we have: ")
print(list(square_of_array))
print("Using numpy power():")
#And here, only numpy library
square_of_array = np.power(base, exponents)
print(square_of_array)

square_of_array = np.power(base,varing_exponents)
print("Using numpy power() but with exponents variation.")
print(square_of_array)
