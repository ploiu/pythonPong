import world, random

class PowerUpManager:
    def __init__(self, ball, players):
        """manager for powerUps. handles placeing powerUps in the world and choosing when and what type the powerUp is"""
        self._ball = ball
        self._players = players
        # time until next attempt to spanw a powerUp takes place
        self.__DEFAULT_POWERUP_TIMER = 15
        self._timeUntilNextPowerUp = self.__DEFAULT_POWERUP_TIMER
        # only 1 powerUp can exist in the world at a time
        self.powerUp = None
        self._powerUpMapping = {
                0: world.SpeedBallPowerUp
            }
        """a dict containing powerUp IDs and the powerUp they''re associated with, used to instantiate the corresponding powerUp when it comes to place one in the world"""
        
    def _create_powerUp(self):
        """creates a random powerUp in the world at a random (but constrained) location"""
        # the max distance from the center that the powerUp can spawn from
        maxDistance = 20
        # the x spawn location
        spawnX = random.randint(-maxDistance, maxDistance)
        spawnY = random.randint(-maxDistance, maxDistance)
        # the powerUp id to spawn in TODO change when we get more powerUps
        powerUpType = random.randint(0, 0)
        # the powerUp to spawn in
        powerUpToSpawn = self._powerUpMapping[powerUpType](spawnX, spawnY, self._ball, self._players)
        self.powerUp = powerUpToSpawn
    
    def tick(self):
        """called periodically in the game loop, used to check for powerUp status and spawn in new powerUps / remove expired ones from the world"""
        # if there's already a powerup, don't change the timer
        if self.powerup is None:
            self._timeUntilNextPowerUp -= 1
            if self._timeUntilNextPowerUp <= 0:
                # reset the timer and attempt to spawn a powerup
                self._timeUntilNextPowerUp = self.__DEFAULT_POWERUP_TIMER
                self._attempt_spawnPowerup()
        elif self.powerup.life <= 0:
            # set our powerup to be none
            self.powerup = None
            
    def _attempt_spawnPowerup(self):
        # if we don't have a powerUp, attempt to generate one
        if self.powerUp is None and random.randint(0, 255) == 69:
            # create a powerUp
            self.create_powerUp()