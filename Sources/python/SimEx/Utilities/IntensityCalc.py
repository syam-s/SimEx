##########################################################################
#                                                                        #
# Copyright (C) 2016-2018 Richard Briggs, Carsten Fortmann-Grote         #
# Contact: Carsten Fortmann-Grote <carsten.grote@xfel.eu>                #
#                                                                        #
# This file is part of simex_platform.                                   #
# simex_platform is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# simex_platform is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
##########################################################################


def calculateLaserIntensity(laser_energy=None):
    """
    Converts the laser energy (in J), pulse length (flat top, in nanoseconds) and spot size (diameter in microns) to intensity in TW/cm^2.
    :param laser_energy: Energy (J)
    :type laser_energy: Number
    """

    if laser_energy is None:
        Energy = float(input("Energy (J) : "))
    else:
        Energy = laser_energy

    SpotSize = float(input("Spot size (diameter in um) : "))
    PulseLength = float(input("Pulse length (ns) : "))

    PulseLength = PulseLength*1e-9
    SpotSize = SpotSize/10000
    SpotArea = 3.14159265359*(0.5*SpotSize)*(0.5*SpotSize)
    Power = Energy/PulseLength
    Intensity = Power/SpotArea
    Intensity = Intensity/1e12

    print("Intensity = ", Intensity, "TW/cm**2")

    return Intensity
