n = int(input("Enter num"))
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()
# output for n=4

#    *
#   * *
#  * * *
# * * * *

# for i in range(0, n//2+1):
#     print(" "*(n-i)+"@"*(2*i+1))
# output for n=6
#       @
#      @@@
#     @@@@@
#    @@@@@@@

# for i in range(n, 0, -1):
#     for j in range(0, n-i):
#         print(end=" ")
#     for j in range(0, i):
#         print("*", end=" ")
#     print()
# * * * *
#  * * *
#   * *
#    *

# for i in range(1, n+1):
#     for j in range(1, 2*n):
#         if (i == n or i+j == n+1 or j-i == n-1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********

# k = 2
# for i in range(1, n+1):
#     for j in range(1, 2*n):
#         if (i+j == n+1 or j-i == n-1):
#             print("*", end="")
#         elif (i == n and j != k):
#             print("*", end="")
#             k = k+2
#         else:
#             print(" ", end="")
#     print()
#    *
#   * *
#  *   *
# * * * *


# for i in range(5):
#     for j in range(5):
#         if (i+j == 2 or j-i == 2 or i-j == 2 or i+j == 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#   *
#  * *
# *   *
#  * *
#   *


# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print("*", end="")
#     for j in range((n-i)*2):
#         print(" ", end="")
#     for j in range(i, 0, -1):
#         print("*", end="")
#     print()
# for i in range(1, n):
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(2*(n-i-1)):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     print()

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# for i in range(9):
#     for j in range(13):
#         if (i == 2 or i == 6 or i+j == 6 or j-i == 6 or i-j == 2 or i+j == 14):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#       *
#      * *
# *************
#  * *     * *
#   *       *
#  * *     * *
# *************
#      * *
#       *
# k = n+(n-5)
# mid = k // 2
# for i in range(n):
#     for j in range(k):
#         if (i == 2 or i == (n-3) or i+j == mid or j-i == mid or i-j == 2 or i+j == k+1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#           *
#          * *
# *********************
#  *     *     *     *
#   *   *       *   *
#    * *         * *
#     *           *
#    * *         * *
#   *   *       *   *
#  *     *     *     *
# *********************
#          * *
#           *


# for i in range(n+1):
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#     print()
# *
# **
# ***
# **
# *

# for i in range(n+1):
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#   *
#  **
# ***
#  **
#   *


# for i in range(n//2+1):
#     for j in range(n//3+1):
#         print(end=" ")
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n, 2*i, -1):
#         print("@", end="")
#     print()
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or j == n-1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#    @@@@@@@
#     @@@@@
#      @@@
#       @
# *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *     *

# for i in range(n//2+2):
#     # for j in range(n//3+1):
#     #     print(end=" ")
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# for i in range(n):
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     for j in range(n):
#         if (i == n//2):
#             print("@", end="")
#         else:
#             print(" ", end="")
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#     print()
#      @
#     @@@
#    @@@@@
#   @@@@@@@
#   *     *
#  **     **
# ***@@@@@***
#  **     **
#   *     *

# for i in range(7):
#     for j in range(5):
#         if ((j == 0 and (i != 0 and i != 6)) or ((i == 0 or i == 6) and j > 0)):
#             print("*", end=" ")
#         else:
#             print(" ", end="")
#     print()
#  * * * *
# *
# *
# *
# *
# *
#  * * * *

# for i in range(7):
#     for j in range(5):
#         if (j == 0 or (j == 4 and (i != 0 and i != 6))) or ((i == 0 or i == 6) and (j > 0 and j < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****

# for i in range(7):
#     for j in range(5):
#         if (j == 0 or i == 0 or i == 3 or i == 6):
#             print("@", end="")
#         else:
#             print(end=" ")
#     print()
# @@@@@
# @
# @
# @@@@@
# @
# @
# @@@@@

# mid = n-4
# for i in range(n):
#     for j in range(n-2):
#         if (j == 0 or (i == 0 or i == mid)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *****
# *
# *
# *****
# *
# *
# *


# for i in range(7):
#     for j in range(6):
#         if ((j == 0 or (j == 4 and (i != 1 and i != 2))) or ((i == 0 or i == 6) and (j > 0 and j < 4)) or (i == 3 and (j == 3 or j == 5))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *****
# *
# *
# *  ***
# *   *
# *   *
# *****

# for i in range(7):
#     for j in range(5):
#         if (j == 0 or j == 4 or (i == 3 and (j > 0 and j < 4))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *   *
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

# for i in range(7):
#     for j in range(5):
#         if (j == 0 or i+j == 4 or i == j+2):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *   *
# *  *
# * *
# **
# * *
# *  *
# *   *


# for i in range(7):
#     for j in range(7):
#         if (j == 0 or j == 6 or (i+j == 6 and i <= 3) or (i == j and i < 3)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *

# for i in range(6):
#     for j in range(6):
#         if (j == 0 or j == 5 or (i == j and i < 5)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# *    *
# **   *
# * *  *
# *  * *
# *   **
# *    *

# for i in range(7):
#     for j in range(5):
#         if (((j == 0 or j == 4) and (i != 0 and i != 6)) or ((i == 0 or i == 6) and (j > 0 and j < 4))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
#  ***
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***

# for i in range(7):
#     for j in range(5):
#         if (j == 0 or ((i == 0 or i == 3) and j != 4)) or (j == 4 and (i == 1 or i == 2)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# ****
# *   *
# *   *
# ****
# *
# *
# *

# for i in range(8):
#     for j in range(5):
#         if (((j == 0 or j == 4) and (i > 0 and i < 6)) or ((i == 0 or i == 6) and (j != 0 and j != 4)) or (i == 5 and j == 1) or (j == 3 and (i == 7))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
#  ***
# *   *
# *   *
# *   *
# *   *
# **  *
#  ***
#    *
