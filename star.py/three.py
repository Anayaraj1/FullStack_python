# Right sided triangle
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

# left sided Triangle

n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i, n):
        print(" ", end=" ")
    print()

# *
# * *
# * * *
# * * * *
# * * * * *

# another pattern

n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

    # * * * * *
    #   * * * *
    #     * * *
    #       * *
    #         *

    # Hill Pattern

n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()


#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
