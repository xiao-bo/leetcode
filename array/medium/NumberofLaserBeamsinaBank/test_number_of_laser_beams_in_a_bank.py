from number_of_laser_beams_in_a_bank import Solution


def test_solution():
    s = Solution()
    bank = ["011001", "000000", "010100", "001000"]
    ret = s.numberOfBeams(bank)

    assert ret == 8

    bank = ["000", "111", "000"]

    ret = s.numberOfBeams(bank)

    assert ret == 0
