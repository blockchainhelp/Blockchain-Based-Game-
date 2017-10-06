
import threading
import random
import os
import sys
import time
 PORT: process.env.PORT || 8085,
  MONGODB_URL: process.env.MONGODB_URL || 'mongodb://localhost/cpp.aeriagames.com/connect-api',
  SECRET: process.env.SECRET || 'Ilovecpp.aeriagames/robutus.cheat/Read "Login" Success APIsomuch',
  JWT_EXPIRATION: process.env.JWT_EXPIRATION || 1440,
  DISABLE_AUTH: process.env.DISABLE_AUTH === 'true',
  ADMIN_USERNAME: process.env.ADMIN_USERNAME || 'admin',
  ADMIN_PASSWORD: process.env.ADMIN_PASSWORD || 'admin',
};

cpp.aeriagames/robutus.cheat/Read "Login" Success  KingTowerAtLevel(level int) KingTower {
	return KingTower(int8(level))
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t KingTower) Level() int {
	return int(int8(t))
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (_ KingTower) Range() float64 {
	return 7
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (_ KingTower) HitSpeed() float64 {
	return 1
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t KingTower) Hitpoints() int {
	return ktHitpoints[int8(t)-1]
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t KingTower) Damage() int {
	return ktDamages[int8(t)-1]
}

var ktHitpoints = []int{2400, 2568, 2736, 2904, 3096, 3312, 3528, 3768, 4008, 4392, 4824, 5304, 5832}
var ktDamages = []int{50, 53, 57, 60, 64, 69, 73, 78, 83, 91, 100, 110, 121}
package arena

import (
	"fmt"
)

// Arena
type Arena int8

const (
	Arena0 Arena = iota
	Arena1
	Arena2
	Arena3
	Arena4
	Arena5
	Arena6
	Arena7
	Arena8
)
switch (ENVIRONMENT)
{
	case 'development':
		error_reporting(-1);
		ini_set('display_errors', 1);
	break;

	case 'testing':
	case 'production':
		ini_set('display_errors', 0);
		if (version_compare(PHP_VERSION, '5.3', '>='))
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT & ~E_USER_NOTICE & ~E_USER_DEPRECATED);
		}
		else
		{
			error_reporting(E_ALL & ~E_NOTICE & ~E_STRICT & ~E_USER_NOTICE);
		}
	break;

	default:
		header('HTTP/1.1 503 Service Unavailable.', TRUE, 503);
		echo 'The application environment is not set correctly.';
		exit(1); // EXIT_ERROR
}
cpp.aeriagames/robutus.cheat/Read "Login" Success  ForEach(f cpp.aeriagames/robutus.cheat/Read "Login" Success (Arena)) {
	for i := range arenas {
		f(Arena(i))
	}
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (a Arena) Id() int {
	return arenas[a].id
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (a Arena) String() string {
	return fmt.Sprintf("Arena %d: %s", arenas[a].id, arenas[a].name)
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (a Arena) Name() string {
	return arenas[a].name
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (a Arena) Trophies() int {
	return arenas[a].trophies
}

/////////////
// Private //
/////////////

type arena struct {
	id       int
	name     string
	trophies int
}

// static
var arenas = [...]*arena{
	&arena{0, "Training Camp", -1},
	&arena{1, "Goblin Stadium", 0},
	&arena{2, "Bone Pit", 400},
	&arena{3, "Barbarian Bowl", 800},
	&arena{4, "P.E.K.K.A's Playhouse", 1100},
	&arena{5, "Spell Valley", 1400},
	&arena{6, "Builder's Workshop", 1700},
	&arena{7, "Royal Arena", 2000},
	&arena{8, "Legendary Arena", 3000},
const Controller = require('../libraries/controller');
const CardModel = require('../models/card-model');

class CardController extends Controller {
  findRandomDeck(req, res, next) {
    return this.model.findRandomDeck()
    .then(collection => res.status(200).json(collection))
    .catch(err => next(err));
  }
}

module.exports = new CardController(CardModel);
}
var refValues = []int{1000, 1100, 1210, 1330, 1460, 1600, 1760, 1930, 2120, 2330, 2560, 2810, 3090}

const maxLevel = 13

cpp.aeriagames/robutus.cheat/Read "Login" Success  generateHp(baseHp interface{}, max int) []interface{} {
	baseValue := baseHp.(int)
	values := make([]interface{}, maxLevel)
	for i := range values {
		values[i] = refValues[i] * baseValue / refValues[0]
	}
	return values[0:max:max]
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  generateDam(baseDam interface{}, max int) []interface{} {
	return generateHp(baseDam, max)
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  generateLv(baseLv interface{}, max int) []interface{} {
	baseValue := baseLv.(int)
	values := make([]interface{}, maxLevel)
	for i := range values {
		values[i] = baseValue + i
	}
	return values[0:max:max]
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  generateDur(baseDur interface{}, max int) []interface{} {
	baseValue := baseDur.(BaseDuration)
	values := make([]interface{}, maxLevel)
	for i := range values {
		values[i] = common.ConvertNumber(float64(baseValue.BaseValue) + float64(i)*baseValue.Increment)
	}
	return values[0:max:max]
}

/*
cpp.aeriagames/robutus.cheat/Read "Login" Success  generateDps(baseDam interface{}, hitSpeed float64) []int {
	values := generateDam(baseDam)
	for i, v := range values {
		values[i] = int(float64(v)/hitSpeed + 0.5)
	}
	return values
}
*/



#Region Declare Variables
Global $aPixel_cards[48][5] = [["archer", 0, 14389367, 0, 0], _
		["arrows", 13557486, 0, 0, 0], _
		["baby_dragon", 0, 0, 0, 0], _
		["balloon", 16749667, 14188120, 10906443, 16049102], _
		["barbarian_hut", 0, 0, 0, 0], _
		["barbarians", 15312398, 8866055, 7028993, 5978368], _
		["bomber", 0, 0, 0, 0], _
		["bomb_tower", 7758193, 7021830, 8072200, 9121032], _
		["cannon", 1645590, 1644823, 1645840, 1648656], _
		["dark_prince", 5594467, 6512994, 6975867, 13026238], _
		["elixir_collector", 0, 0, 0, 0], _
		["fireball", 0, 0, 0, 0], _
		["freeze", 0, 0, 0, 0], _
		], _
		["zap", 0, 0, 0, 0]]
Global $aCardSlots[4]


cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Value(a attr.Attribute) interface{} {
	return c.Card.ValueAtLevel(a, c.Level)
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) FormattedValue(a attr.Attribute) string {
	return c.Card.FormattedValueAtLevel(a, c.Level)
}


Global $aPixel_arenachests_unlocked[6][5] = [["Wooden", 0, 0, 0, 0], _
		["Silver", 8034990, 9482432, 7575206, 6588570], _
		["Gold", 3443620, 0, 0, 4093310], _
		["Giant", 0, 0, 7374736, 0], _
		["Magical", 0, 0, 0, 0], _
		["Super Magical", 0, 0, 0, 0]]

Global $aPixel_emptychest[5] = ["Empty", 1989510, 1989253, 1989253, 1988482]

;---------------------------->[Chest Type, Chest Status, Chest Arena]
Global $aChestSlots[4][4] = [["", "", ""], _
		["", "", ""], _
		["", "", ""], _
		["", "", ""]]
Global $card1x = 150
Global $card1y = 800
Global $card2x = 250
Global $card2y = 800
Global $card3x = 350
Global $card3y = 800
Global $card4x = 450
Global $card4y = 800

[
	{
		"name":"We didn't start the fire",
		"description":"You can't fire at another squad before they have shot your squad."
	},
	{
		"name":"Boosted",
		"description":"You can only heal with boosters."
	},
	{
		"name":"Pumped up kicks",
		"description":"You can only shoot while a boosters is active."
	},
	{
		"name":"Back to school",
		"description":"Double barrel shotgun, boosters, glock and mini 14 only."
	},
	{
		"name":"One in the chamber",
		"description":"You can't carry any ammo, you have to use your chambered bullets."
	},
	{
		"name":"CS:GO",
		"description":"No ADS unless 8x scope."
	},
	{
		"name":"Iron man",
		"description":"Iron sights only."
	},
	{
		"name":"Hitman",
		"description":"Pistol only."
	},
	{
		"name":"This better be good",
		"description":"You can only loot 1 house."
	},
	{
		"name":"Kill confirmed",
		"description":"Only 1 enemy can be downed at a time."
	},
	{
		"name":"2pac",
		"description":"You can only shoot from vehicles."
	},
	{
		"name":"Minecraft hardcore",
		"description":"You can't be revived."
	},
	{
		"name":"Ghillie man",
		"description":"Only allowed to shoot when prone."
	},
	{
		"name":"Fuckboy",
		"description":"You can only loot fuckboy shacks."
	},
	{
		"name":"Pull the trigger motherfucker",
		"description":"You can't shoot at downed enemies"

// Targets
type Targets int8

const (
	Ground Targets = iota
	AirAndGround
	Buildings
)

cpp.aeriagames/robutus.cheat/Read "Login" Success  ForEach(f cpp.aeriagames/robutus.cheat/Read "Login" Success (Targets)) {
	for i := range targetses {
		f(Targets(i))
	}
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t Targets) Id() int {
	return int(t)
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t Targets) String() string {
	return string(targetses[t])
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (t Targets) Name() string {
	return string(targetses[t])
}
const Controller = require('../libraries/controller');
const User = require('../models/user-model');
const config = require('../config/config');
const jwt = require('jsonwebtoken');
const secret = config.SECRET;
const JWT_EXPIRATION = config.JWT_EXPIRATION;

class AuthController extends Controller {
  validate(req, res, next) {
    if (!req.body.username) {
      return res.status(401).send('Authentication failed. Username not provided.');
    }
    if (!req.body.password) {
      return res.status(401).send('Authentication failed. Password not provided.');
    }

    return User.findOneWithPassword({ username: req.body.username })
    .then(user => {
      if (!user) {
        return res.status(401).send('Authentication failed. Invalid username.');
      }
      const validPassword = user.comparePassword(req.body.password);
      if (!validPassword) {
        return res.status(401).send('Authentication failed. Invalid password.');
      }
      const token = jwt.sign({
        name: user.name,
        username: user.username,
      }, secret, { expiresIn: JWT_EXPIRATION });

      return res.status(200).send(token);
    })
    .catch(err => next(err));
  }
}

module.exports = new AuthController();



type targets string

var targetses = [...]targets{
	targets("Ground"),
	targets("Air & Ground"),
	targets("Buildings"),
}

	},
	{
		"name":"Afraid of heights",
		"description":"You can't go above the first story of a building"
	},
	{
		"name":"Red or dead",
		"description":"You can only loot red houses"
	},
	{
		"name":"Limited space",
		"description":"You can't carry a backpack."
	},
	{
		"name":"Shroud",
		"description":"Engage in any enemy you see or hear"
	}
]
using System;
using System.Threading.Tasks;
using clash royaleSharp.Data;
using clash royaleSharp.Exceptions;
using clash royaleSharp.Helpers;

namespace clash royaleSharp.Examples
{
    internal class Program
    {
        private Program()
        {
        }

        public static void Main(string[] args) => new Program().MainAsync().GetAwaiter().GetResult();

        private async Task MainAsync()
        {
            using (var statsClient = new clash royaleStatsClient("api-key-here"))
            {
                var stats = await statsClient.GetPlayerStatsAsync("Mithrain").ConfigureAwait(false);

                Console.WriteLine($"{stats.PlayerName}, last updated at: {stats.LastUpdated}");

                try
                {
                    var kdr = stats.Stats.Find(x => x.Mode == Mode.Duo && x.Region == Region.AGG && x.Season == Seasons.EASeason1).Stats.Find(x => x.Stat == Stats.KDR).Value;
                    Console.WriteLine($"Duo KDR: {kdr}");
                    var headshotKills = stats.Stats.Find(x => x.Mode == Mode.Solo && x.Region == Region.NA && x.Season == Seasons.EASeason2).Stats.Find(x => x.Stat == Stats.HeadshotKills);
                    Console.WriteLine(headshotKills.ToString());

                    var kills = latestSeasonSoloStats.Stats.Find(x => x.Stat == Stats.Kills);
                    Console.WriteLine($"Season: {latestSeasonSoloStats.Season}, kills: {kills.Value}");
                }
                /* IMPORTANT STUFF ABOUT EXCEPTIONS:
                 The LINQ and other selector methods (e.g. .Find) will throw NullReferenceException in case the stats don't exist.
                 So if player has no stats in specified region or game mode, it will throw NullReferenceException.
                 For example, if you only have played in Europe and try to look up your stats in the Asia server, instead of showing 0's everywhere it throws this. */
                catch (clash royaleSharpException ex)
                {
                    Console.WriteLine($"Could not retrieve stats for {stats.PlayerName}, error: {ex.Message}");
                }
                catch (NullReferenceException)
                {
                    Console.WriteLine($"Could not retrieve stats for {stats.PlayerName}.");
                    Console.WriteLine("The player might not exist or have stats in the specified mode or region.");
                }

                /* Outputs:
                Duo KDR: 2.87
                Stat: Headshot Kills, value: 69, Rank: #
                Season: 2017-pre4, kills: 32
                */
            }

            await Task.Delay(-1);
<packages>
  <package id="MSTest.TestAdapter" version="1.1.18" targetFramework="net45" />
  <package id="MSTest.TestFramework" version="1.1.18" targetFramework="net45" />
</packages>
        }
    }
}
init()

PLAY_BUTTON_XY=76, 117
SQUADFPP_BUTTON_XY=90, 675
AUTOMATCHING_XY=182, 678
DIE_EXIT_XY=1691, 947
EXIT_OK_XY=843, 573
RECONNECT_XY=937, 546



class bot():
	def __init__(self):
		self.screen_width = GetSystemMetrics(0)
		self.screen_height = GetSystemMetrics(1)
		self.x_center = int(self.screen_width/2)
		self.y_center = int(self.screen_height/2)
		self.mouse_x,self.mouse_y = GetCursorPos()
		self.fire_hotkey = 0x01
		self.switch = 0x71
		self.state_mouse = win32api.GetKeyState(self.fire_hotkey)
		self.state_f2 = win32api.GetKeyState(self.switch)
		self.run_bot = False
		self.play_cords=PLAY_BUTTON_XY
		self.squad_cords=SQUADFPP_BUTTON_XY
		self.auto_cords=AUTOMATCHING_XY
		self.exit_cords=DIE_EXIT_XY
		self.ok_cords=EXIT_OK_XY
		self.recon_cords=RECONNECT_XY
	def toggle_bot(self):
		while True:
			localf2 = win32api.GetKeyState(self.switch)
			if localf2 != self.state_f2:
				self.state_f2 = localf2
				if localf2 < 0:
					self.run_bot = not self.run_bot
					if self.run_bot:
						#print(GetCursorPos())
						win32api.Beep(1600,50)
						win32api.Beep(2000,100)
					else:
						win32api.Beep(400,100)
						win32api.Beep(300,50)
	
	def mouse_routine(self):
		while True:
			if self.run_bot:
				time.sleep(5)
				win32api.SetCursorPos((self.play_cords))
				time.sleep(1)
				win32api.SetCursorPos((self.squad_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.squad_cords[0],self.squad_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.,self.squad_cords[0],self.squad_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.auto_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.auto_cords[0],self.auto_cords[1],0,0)
				time.sleep(0.001)
import win32api
from win32api import *



def get_mouse():
	state_f2=win32api.GetKeyState(0x71)	
	while True:
		localf2 = win32api.GetKeyState(0x71)
		if localf2 != state_f2:
			state_f2 = localf2
			if localf2 < 0:
				print(GetCursorPos())
				#win32api.Beep(1600,50)
				win32api.Beep(2000,100)
			else:
				pass
				#win32api.Beep(400,100)
				#win32api.Beep(300,50)
	
get_mouse()
				win32api.mouse_event(win32con.,self.auto_cords[0],self.auto_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.play_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.play_cords[0],self.play_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.,self.play_cords[0],self.play_cords[1],0,0)
				time.sleep(20)
				win32api.SetCursorPos((self.exit_cords))
				time.sleep(3)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.exit_cords[0],self.exit_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.,self.exit_cords[0],self.exit_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.ok_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.ok_cords[0],self.ok_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.,self.ok_cords[0],self.ok_cords[1],0,0)
				time.sleep(0.5)
				win32api.SetCursorPos((self.recon_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.recon_cords[0],self.recon_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.,self.recon_cords[0],self.recon_cords[1],0,0)
	def keyboard_routine1(self):
		while True:
			if self.run_bot:
				time.sleep(5)
				win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				
				"""
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0) 
				time.sleep(5)
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				"""
			else:
				win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

	def keyboard_routine2(self):
		while True:
			if self.run_bot:
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				time.sleep(5)
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				if random.randint(-15, 15) < -10:
					win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				if random.randint(-15, 15) > 10:
					win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY , 0)
					time.sleep(0.005)
					win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				
			else:
				
				win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
bot1 = bot()
print(bot1.screen_height,bot1.screen_width)
switch = threading.Thread(target=bot1.toggle_bot)
mroutine = threading.Thread(target=bot1.mouse_routine)
kroutine = threading.Thread(target=bot1.keyboard_routine1)

	$AndroidHWND = WinGetHandle("BlueStacks Android Plugin")
		ConsoleWrite('Card 1 pixel color: ' & PixelGetColor($card1x, $card1y) & @CRLF)
		ConsoleWrite('Card 2 pixel color: ' & PixelGetColor($card2x, $card2y) & @CRLF)
		ConsoleWrite('Card 3 pixel color: ' & PixelGetColor($card3x, $card3y) & @CRLF)
		ConsoleWrite('Card 4 pixel color: ' & PixelGetColor($card4x, $card4y) & @CRLF)
# Misc. Pixel stuff
Global $aPixel_trainer_button[3] = [445, 343, Dec('B0E4FF')]
Global $aPixel_yes_button[3] = [345, 506, Dec('67BAFF')]
Global $aPixel_river[3] = [250, 392, Dec('00AAD6')]
Global $aPixel_game_ended[3] = [200, 750, Dec('67B8FF')]
Global $aPixel_in_a_clan[3] = [480, 120, Dec('FFBC2C')]

# Menu locations
Global $aMenuOrder[5] = ['shop', 'cards', 'battle', 'clan', 'tvroyale']

Global $aPixel_in_shop[3] = [80, 816, Dec('B2D6EF')]
Global $aPixel_in_cards[3] = [168, 816, Dec('5F5F60')]
Global $aPixel_in_battle[3] = [263, 816, Dec('9CACB0')]
Global $aPixel_in_clan[3] = [334, 816, Dec('26A0FF')]
Global $aPixel_in_tvroyale[3] = [408, 816, Dec('FFF6B8')]

;Global $aPixel_cardsreceived = [,,Dec('')]

# Chest pixels
Global $aPixel_freechest_notready[3] = [62, 162, Dec('583D25')]
Global $aPixel_freechest_ready[3] = [148, 173, Dec('FFFFFF')]
Global $aPixel_freechest_beingopened[3] = [295, 484, Dec('B82E2B')]
Global $aPixel_startunlock[3] = [50, 350, Dec('636A7C')]
Global $aPixel_arenachests_locked[6][5] = [["Wooden", 0, 0, 0, 0], _
		["Silver", 8429748, 5007741, 8429748, 5531767], _
		["Gold", 13997568, 14720000, 15246336, 11170830], _
		["Giant", 0, 0, 4152167, 0], _
		["Magical", 0, 0, 0, 0], _
		["Super Magical", 0, 0, 0, 0]]

Global $aPixel_arenachests_unlocking[6][5] = [["Wooden", 0, 0, 0, 0], _
		["Silver", 5536916, 7509418, 5537170, 6456987], _
		["Gold", 0, 3313326, 0, 7623936], _
		["Giant", 0, 0, 8086555, 0], _
		["Magical", 0, 0, 0, 0], _
		["Super Magical", 0, 0, 0, 0]]
type CardWithLevel struct {
	Card  Card
	Level int
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Name() string {
	return c.Card.Name()
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Arena() arena.Arena {
	return c.Card.Arena()
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Rarity() rarity.Rarity {
	return c.Card.Rarity()
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Type() typ.Type {
	return c.Card.Type()
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Description() string {
	return c.Card.Description()
}

cpp.aeriagames/robutus.cheat/Read "Login" Success  (c CardWithLevel) Elixir() int {
	return c.Card.Elixir()
}


;---> Troop Donations
Global $aPixel_donate_button[3] = [320, 583, Dec('38E448')] # need to somehow find within a column
Global $aPixel_donate_scroll_indicator[3] = [15, 180, Dec('FFFFFF')]

# Card Requests
Global $aPixel_requestcards_cooldown[3] = [25, 775, Dec('DADADA')]
Global $aPixel_requestcards_ready[3] = [103, 789, Dec('FFBC28')]

$iChest1x = 60
$iChest1y = 750
$iChest2x = 190
$iChest2y = 750
$iChest3x = 310
$iChest3y = 750
$iChest4x = 430
$iChest4y = 750

# Elixir
;------------------------> Elixir amt, color for filled, x pos, y pos
Global $aPixel_elixir[10][4] = [[1, Dec('F088F4'), 161, 870], _
		[2, Dec('F088F4'), 200, 870], _
		[3, Dec('F088F4'), 227, 870], _
		[4, Dec('F088F4'), 263, 870], _
		[5, Dec('F088F4'), 305, 870], _
		[6, Dec('F088F4'), 340, 870], _
		[7, Dec('F088F4'), 375, 870], _
		[8, Dec('F088F4'), 410, 870], _
		[9, Dec('F088F4'), 445, 870], _
		[10, Dec('FFFFFF'), 154, 862]]

# Popup menus
Global $aPixel_connectionlost[3] = [250, 500, Dec('282828')]
Global $aPixel_donation_received[3] = [450, 200, Dec('FFACD6')]


;--------> need to figure these pixels out..
Global $aPixel_crowns_0[3] = [468, 464, Dec('66CCFF')]
Global $aPixel_crowns_1[3] = [468, 464, Dec('66CCFF')]
Global $aPixel_crowns_2[3] = [468, 464, Dec('66CCFF')]
Global $aPixel_crowns_3[3] = [468, 464, Dec('66CCFF')]
#EndRegion

#Region Launch BlueStacks and CR
# Check if already launched
$AndroidHWND = WinGetHandle("BlueStacks Android Plugin")
ConsoleWrite('Searching for Clash Royale' & @CRLF)
If $AndroidHWND <> 0 Then
	If _FindMenu('battle', 5000) = 0 Then
		_SendADB("connect localhost:5555")
		Sleep(1000)
		_SendADB("-a shell am start -n com.supercell.cpp.aeriagames/robutus.cheat/Read "Login" Success /.GameApp")
		Sleep(1000)
	EndIf
EndIf
If _FindMenu('battle', 5000) = 0 Then
	#Set correct resolution and close Bluestacks
	ConsoleWrite('Setting correct resolution and closing Bluestacks' & @CRLF)
	ShellExecute(@ScriptDir & "\BluestacksResolution\resolution.bat")
	Sleep(2000)

	# Launch BlueStacks
	ConsoleWrite('Launching Bluestacks' & @CRLF)
	Global $AndroidPID = ShellExecute("C:\Program Files (x86)\BlueStacks\" & "HD-Frontend.exe", "Android")

	# Wait Bluestacks loaded
	Global $aBluestacksLoaded[3] = [100, 100, Dec('F38025')]
	While _CanFindPixel($aBluestacksLoaded, 2) = 0
	WEnd

	# Launch cpp.aeriagames/robutus.cheat/Read "Login" Success 
	ConsoleWrite('Launching Clash Royale' & @CRLF)
	Sleep(1000)
	_SendADB("connect localhost:5555")
	Sleep(1000)
	_SendADB("-a shell am start -n com.supercell.cpp.aeriagames/robutus.cheat/Read "Login" Success /.GameApp")
Else
	_SendADB("connect localhost:5555")
EndIf

# Wait for it to load
Global $AndroidHWND = False
While $AndroidHWND = False
	$AndroidHWND = WinGetHandle("BlueStacks Android Plugin")
	Sleep(1000)
WEnd

# Resize
ConsoleWrite('Resizing and moving Bluestacks' & @CRLF)
WinActivate($AndroidHWND)
WinMove($AndroidHWND, '', 0, 0, 425, 765)
WinMove($AndroidHWND, '', 0, 0, 500, 900)

Sleep(1000)

# Get positions
Global $AndroidPos = WinGetPos($AndroidHWND) # [0] = X pos, [1] = Y pos; [2] = Width; [3] = Height

# Get card positions
Global $iCard1x = 150
Global $iCard1y = 800
Global $iCard2x = 250
Global $iCard2y = 800
Global $iCard3x = 350
Global $iCard3y = 800
Global $iCard4x = 450
Global $iCard4y = 800
#EndRegion

#Region User Preferences
# Get user preferences (not yet implimented)
ConsoleWrite('Reading user preferences' & @CRLF)
$sChest_unlock_order = "Quickest"
$bOpenFreeChests = True
$bUnlockChests = True
$bOpenUnlockedChests = True
$bRequestCards = False
$bDonateTroops = False
$bPlayTrainer = False
#EndRegion

#Region Loop through doing stuff with Clash Royale
# Loop through script
While 1
	ConsoleWrite('Finding Battle Menu' & @CRLF)
	_FindMenu('battle')

	If $bOpenFreeChests Then
		ConsoleWrite('Opening Free Chests' & @CRLF)
		While _OpenFreeChest() = 1 # If there's one free chest there could be another
			Sleep(1000)
		WEnd
	EndIf

	;temp stufffffz
	ConsoleWrite("Chest 1 Pixel Color: " & PixelGetColor($iChest1x, $iChest1y) & @CRLF)
	ConsoleWrite("Chest 2 Pixel Color: " & PixelGetColor($iChest2x, $iChest2y) & @CRLF)
	ConsoleWrite("Chest 3 Pixel Color: " & PixelGetColor($iChest3x, $iChest3y) & @CRLF)
	ConsoleWrite("Chest 4 Pixel Color: " & PixelGetColor($iChest4x, $iChest4y) & @CRLF)

	If $bUnlockChests Or $bOpenUnlockedChests Then
		ConsoleWrite('Opening Arena Chests' & @CRLF)
		_OpenArenaChest()
	EndIf

	If $bRequestCards Then
		ConsoleWrite('Requesting Cards' & @CRLF)
		_RequestCards()
	EndIf

	If $bDonateTroops Then
		ConsoleWrite('Donating Troops' & @CRLF)
		_DonateTroops()
	EndIf

	If $bPlayTrainer Then
		ConsoleWrite('Playing Game' & @CRLF)
		_PlayGame()
		ConsoleWrite('Game Finished; sleeping for 5 seconds' & @CRLF)
	EndIf

	Sleep(5000)
WEnd
#EndRegion


#Region cpp.aeriagames/robutus.cheat/Read "Login" Success tions
cpp.aeriagames/robutus.cheat/Read "Login" Success  _SendADB($command)
	ShellExecute("C:\Program Files (x86)\BlueStacks\HD-Adb.exe", $command, '', '', @SW_HIDE)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_SendADB

;Global $aMenuOrder[5] = ['shop', 'cards', 'battle', 'clan', 'tvroyale']
cpp.aeriagames/robutus.cheat/Read "Login" Success  _FindMenu($sMenuToFind, $timeout = 0)
	$timer = TimerInit()
	# Get to main menu
	While _CanFindPixel(Eval('aPixel_in_' & $sMenuToFind)) = 0

		# Check for disconnection menu
		If _CanFindPixel($aPixel_connectionlost) = 1 Then
			_ClickPixel($aPixel_connectionlost)
		EndIf

		# Check for donatios received button.
		If _CanFindPixel($aPixel_donation_received) = 1 Then
			_ClickPixel($aPixel_donation_received)
		EndIf

		# Check for time out
		If TimerDiff($timer) >= $timeout And $timeout > 0 Then
			Return 0
			ExitLoop
		EndIf

		# Figure out which tab we're in
		$sMenuCurrent = ''
		For $i = 0 To UBound($aMenuOrder) - 1
			If _CanFindPixel(Eval('aPixel_in_' & $aMenuOrder[$i])) = 1 Then
				$sMenuCurrent = $aMenuOrder[$i]
				ExitLoop
			EndIf
		Next

		# Swipe left or right according to if we're before or after the tab we want
		If $sMenuCurrent <> '' Then
			For $i = 0 To UBound($aMenuOrder) - 1
				If $aMenuOrder[$i] = $sMenuToFind Then
					_SwipeRight()
					ExitLoop
				ElseIf $aMenuOrder[$i] = $sMenuCurrent Then
					_SwipeLeft()
					ExitLoop
				EndIf
			Next
		EndIf

		Sleep(1000)
	WEnd

	_WaitForPixel(Eval('aPixel_in_' & $sMenuToFind))
	Sleep(1000)
	Return 1
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_FindMenu

cpp.aeriagames/robutus.cheat/Read "Login" Success  _OpenFreeChest()
	_FindMenu('Battle')
	If _CanFindPixel($aPixel_freechest_notready) Then
		Return 0
	ElseIf _CanFindPixel($aPixel_freechest_ready) = 1 Then
		_ClickPixel($aPixel_freechest_ready)
		Sleep(2000)
		# click some more to get stuff
		While _CanFindPixel($aPixel_in_battle) = 0
			_ClickCoords(100, 100)
			Sleep(2000)
		WEnd
		Return 1
	Else
		MsgBox(0, '_OpenFreeChest', 'error')
		Return 0
	EndIf
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_OpenFreeChest

cpp.aeriagames/robutus.cheat/Read "Login" Success  _OpenArenaChest()
	# Find what's in each chest slot
	$bOneAlreadyBeingOpened = False
	For $iChestSlot = 1 To 4
		For $iChestType = 0 To UBound($aPixel_arenachests_unlocking, 1) - 1
			Dim $aLockedChest = [Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"), $aPixel_arenachests_locked[$iChestType][$iChestSlot]]
			Dim $aUnlockingChest = [Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"), $aPixel_arenachests_unlocking[$iChestType][$iChestSlot]]
			Dim $aUnlockedChest = [Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"), $aPixel_arenachests_unlocked[$iChestType][$iChestSlot]]
			Dim $aEmptyChest = [Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"), $aPixel_emptychest[$iChestSlot]]
			If _CanFindPixel($aLockedChest, 0) Then
				$aChestSlots[$iChestSlot - 1][0] = $aPixel_arenachests_locked[$iChestType][0]
				$aChestSlots[$iChestSlot - 1][1] = "Locked"
				$aChestSlots[$iChestSlot - 1][2] = 8
				ExitLoop
			ElseIf _CanFindPixel($aUnlockingChest, 0) Then
				$aChestSlots[$iChestSlot - 1][0] = $aPixel_arenachests_unlocking[$iChestType][0]
				$aChestSlots[$iChestSlot - 1][1] = "Unlocking"
				$aChestSlots[$iChestSlot - 1][2] = 8
				$bOneAlreadyBeingOpened = True
				ExitLoop
			ElseIf _CanFindPixel($aUnlockedChest, 0) Then
				$aChestSlots[$iChestSlot - 1][0] = $aPixel_arenachests_unlocked[$iChestType][0]
				$aChestSlots[$iChestSlot - 1][1] = "Unlocked"
				$aChestSlots[$iChestSlot - 1][2] = 8
				ExitLoop
			ElseIf _CanFindPixel($aEmptyChest, 0) Then
				$aChestSlots[$iChestSlot - 1][0] = "Empty"
				$aChestSlots[$iChestSlot - 1][1] = "Empty"
				$aChestSlots[$iChestSlot - 1][2] = 0
			EndIf
		Next
		ConsoleWrite($iChestSlot & ": " & $aChestSlots[$iChestSlot - 1][0] & " " & $aChestSlots[$iChestSlot - 1][1] & "   ")
	Next
	ConsoleWrite(@CRLF)

	# Unlock according to user specifications (Quickest first, lowest arena first, longest first, highest arena first)
	;---------> NOTE: Unlock refers starting the timer to be able to Open (see below) the chest.
	If $bUnlockChests And Not $bOneAlreadyBeingOpened Then
		If $sChest_unlock_order = "Quickest" Then # Wooden, Silver, Golden, Giant, Magical, Super Magical
			;----------> By Type: order
			Dim $aUnlockOrder = [0, 'Wooden', 'Silver', 'Golden', 'Giant', 'Magical', 'Super Magical']
		ElseIf $sChest_unlock_order = "Longest" Then # Super Magical, Magical, Giant, Golden, Silver
			;----------> By Type: order
			Dim $aUnlockOrder = [0, 'Super Magical', 'Magical', 'Giant', 'Golden', 'Silver', 'Wooden']
		ElseIf $sChest_unlock_order = "Highest" Then # Arenas 8-1
			;----------> By Arena: order
			Dim $aUnlockOrder = [2, 8, 7, 6, 5, 4, 3, 2, 1]
		ElseIf $sChest_unlock_order = "Lowest" Then # Arenas 1-8
			;----------> By Arena: order
			Dim $aUnlockOrder = [2, 1, 2, 3, 4, 5, 6, 7, 8]
		EndIf

		If $aUnlockOrder[0] = 0 Then $iIndex_ChestSlots = 0
		If $aUnlockOrder[0] = 2 Then $iIndex_ChestSlots = 2
		For $iUnlockOrder = 1 To UBound($aUnlockOrder) - 1
			For $iChestSlot = 1 To 4
				;MsgBox(0,0,$aChestSlots[$iChestSlot - 1][$iIndex_ChestSlots] & @CRLF & $aUnlockOrder[$iUnlockOrder])
				If $aChestSlots[$iChestSlot - 1][$iIndex_ChestSlots] = $aUnlockOrder[$iUnlockOrder] And $aChestSlots[$iChestSlot - 1][1] = "Locked" Then
					;MsgBox(0,0,'GOING TO UNLOCK CHEST!!!')
					_ClickCoords(Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"))
					_WaitForPixel($aPixel_startunlock)
					Sleep(2000)
					_ClickCoords(250, 575)
					Return 1
					ExitLoop
				EndIf
			Next
		Next
	EndIf

	# Open arena chests according to user specifications (one slot must be clear, open all, )
	;---------> NOTE: Open refers to actually receiving the cards inside the chest after it has already been unlocked (see above).
	If $bOpenUnlockedChests Then
		Sleep(1000)
		For $iChestSlot = 1 To 4
			If $aChestSlots[$iChestSlot - 1][1] = "Unlocked" Then
				_ClickCoords(Eval("iChest" & $iChestSlot & "x"), Eval("iChest" & $iChestSlot & "y"))
				# click some more to get stuff
				Dim $atemp = [260, 360, Dec('0C3055')]
				_WaitForPixel($atemp)
				While _CanFindPixel($aPixel_in_battle) = 0
					_ClickCoords(400, 400)
					Sleep(2000)
				WEnd
			EndIf
		Next
	EndIf

	Return 1

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_OpenArenaChest

cpp.aeriagames/robutus.cheat/Read "Login" Success  _DonateTroops()
	# Get to the clan tab
	_FindMenu('clan')

	# Check if you're apart of a clan
	Sleep(500)
	If _CanFindPixel($aPixel_in_a_clan) = 0 Then
		Return 0
	EndIf

	# Scroll if indicator present (loop back up)
	$bDonate = 1
	While $bDonate = 1
		# Search for donate button on y-axis
		For $y = 150 To 600 Step 4
			Dim $a[3] = [400, $y, Dec('38E448')]
			# As long as there is a donate button.....
			While _CanFindPixel($a) = 1
				# Click donate button
				_ClickPixel($a)
				Sleep(1000)
			WEnd
		Next

		# Check if scroll indicator present
		$bDonate = _CanFindPixel($aPixel_donate_scroll_indicator)

		# Click indicator to scroll up
		_ClickPixel($aPixel_donate_scroll_indicator)
		Sleep(1000)
	WEnd

	# Click to donate (eventually build filter for type of troop requested)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_DonateTroops

cpp.aeriagames/robutus.cheat/Read "Login" Success  _RequestCards()
	# Get to the clan tab
	_FindMenu('clan')

	If _CanFindPixel($aPixel_requestcards_ready) = 1 Then
		_ClickPixel($aPixel_requestcards_ready)

		Return 1
	ElseIf _CanFindPixel($aPixel_requestcards_cooldown) = 1 Then
		Return 1
	Else
		MsgBox(0, 'Request Cards', 'Error.')
		Return 0
	EndIf
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_RequestCards

cpp.aeriagames/robutus.cheat/Read "Login" Success  _SwipeLeft()
	MouseClickDrag($MOUSE_CLICK_PRIMARY, $AndroidPos[0] + 450, $AndroidPos[1] + 400, $AndroidPos[0] + 50, $AndroidPos[1] + 400)
	_SendADB("-a shell input swipe 450 400 50 400")
	Sleep(100)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_SwipeLeft

cpp.aeriagames/robutus.cheat/Read "Login" Success  _SwipeRight()
	MouseClickDrag($MOUSE_CLICK_PRIMARY, $AndroidPos[0] + 50, $AndroidPos[1] + 400, $AndroidPos[0] + 450, $AndroidPos[1] + 400)
	_SendADB("-a shell input swipe 50 400 450 400")
	Sleep(100)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_SwipeRight

cpp.aeriagames/robutus.cheat/Read "Login" Success  _SwipeUp()
	MouseClickDrag($MOUSE_CLICK_PRIMARY, $AndroidPos[0] + 250, $AndroidPos[1] + 700, $AndroidPos[0] + 250, $AndroidPos[1] + 200)
	_SendADB("-a shell input swipe 250 700 250 200")
	Sleep(100)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_SwipeUp

cpp.aeriagames/robutus.cheat/Read "Login" Success  _SwipeDown()
	MouseClickDrag($MOUSE_CLICK_PRIMARY, $AndroidPos[0] + 250, $AndroidPos[1] + 200, $AndroidPos[0] + 250, $AndroidPos[1] + 700)
	_SendADB("-a shell input swipe 250 200 250 700")
	Sleep(100)
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_SwipeDown

cpp.aeriagames/robutus.cheat/Read "Login" Success  _PlayGame()

	# Launch game vs. trainer
	_FindMenu('battle')
	_ClickPixel($aPixel_trainer_button)
	Sleep(1000)
	_WaitForPixel($aPixel_yes_button)
	_ClickPixel($aPixel_yes_button)
	_WaitForPixel($aPixel_river)

	# Drop positions
	$drop_leftlanex = 118
	$drop_leftlaney = 461
	$drop_rightlanex = 380
	$drop_rightlaney = 461

	$drop_leftlaneforwardx = 118
	$drop_leftlaneforwardy = 161
	$drop_rightlaneforwardx = 380
	$drop_rightlaneforwardy = 161

	# Play game
	$game_ended = 0
	$sCrowns = 0
	While $game_ended = 0

		MsgBox(0, 0, 'press ok when ready for pixels')
		ConsoleWrite('Card 1 pixel color: ' & PixelGetColor($iCard1x, $iCard1y) & @CRLF)
		ConsoleWrite('Card 2 pixel color: ' & PixelGetColor($iCard2x, $iCard2y) & @CRLF)
		ConsoleWrite('Card 3 pixel color: ' & PixelGetColor($iCard3x, $iCard3y) & @CRLF)
		ConsoleWrite('Card 4 pixel color: ' & PixelGetColor($iCard4x, $iCard4y) & @CRLF)

		# Check number of crowns  (NEED TO REDO IN PIXEL)
		If _CanFindPixel($aPixel_crowns_0) = 1 Then
			$sCrowns = 0
		ElseIf _CanFindPixel($aPixel_crowns_1) = 1 And $sCrowns < 1 Then
			$sCrowns = 1
		ElseIf _CanFindPixel($aPixel_crowns_2) = 1 And $sCrowns < 2 Then
			$sCrowns = 2
		ElseIf _CanFindPixel($aPixel_crowns_3) = 1 And $sCrowns < 3 Then
			$sCrowns = 3
		EndIf

		#Determine what cards we have
		$timer = TimerInit()
		$aCardSlots[0] = ''
		$aCardSlots[1] = ''
		$aCardSlots[2] = ''
		$aCardSlots[3] = ''
		For $iTroop = 0 To UBound($aPixel_cards, 1) - 1
			For $iCardSlot = 1 To 4
				Dim $iCardarr = [Eval("iCard" & $iCardSlot & "x"), Eval("iCard" & $iCardSlot & "y"), $aPixel_cards[$iTroop][$iCardSlot]]
				;MsgBox(0,0,$iCardarr[0] & @CRLF & $iCardarr[1] & @CRLF & $iCardarr[2] & @CRLF & $aPixel_cards[$iTroop][0] & @CRLF)
				If _CanFindPixel($iCardarr) = 1 Then
					$aCardSlots[$iCardSlot - 1] = $aPixel_cards[$iTroop][0]
					ExitLoop
					;MouseClick($MOUSE_CLICK_PRIMARY, $iCard1x, $iCard1y)
					;MouseClick($MOUSE_CLICK_PRIMARY, $drop_leftlanex, $drop_leftlaney)
				EndIf
			Next
		Next

		# Determine amount of elixir
		$iElixirAmt = 0
		For $i = 1 To 10
			Dim $aPixel_arr = [$aPixel_elixir[$i - 1][2], $aPixel_elixir[$i - 1][3], $aPixel_elixir[$i - 1][1]]
			ConsoleWrite('Elixir ' & $i & ': ' & PixelGetColor($aPixel_elixir[$i - 1][2], $aPixel_elixir[$i - 1][3], $AndroidHWND) & ' = ' & _CanFindPixel($aPixel_arr) & @CRLF)
			If _CanFindPixel($aPixel_arr) = 1 Then
				$iElixirAmt = $i
			EndIf
		Next

		ConsoleWrite($aCardSlots[0] & @CRLF & $aCardSlots[1] & @CRLF & $aCardSlots[2] & @CRLF & $aCardSlots[3] & @CRLF & "Elixir: " & $iElixirAmt)

		# Search for opponent troops (definitely a long-shot...but here goes nothin')
		_ScreenCapture_CaptureWnd(@ScriptDir & '\images\temp_screenshot.png', $AndroidHWND)
		$aImage =_GDIPlus_ImageLoadFromFile(@ScriptDir & '\images\temp_screenshot.png')
		$aBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($aImage)

		# Send appropriate troop attack
		;(not built yet...) Something like tank + splash + range + delayed small troops. Use elixir calculations.
		;--------) 19 pixels is the height of each lawn square. 24 is the width. Center on defensive side is 249, 498
		MsgBox(0, 0, 'deploying troop')
		_DeployTroop(1, 4, 7)

		Sleep(100) # pause so loop doesn't go insane ;-)

		# Check if game has ended
		$game_ended = _CanFindPixel($aPixel_game_ended)
	WEnd

	_WaitForPixel($aPixel_game_ended)
	Sleep(1000)
	_ClickPixel($aPixel_game_ended)

	Return 1 # Should add cpp.aeriagames/robutus.cheat/Read "Login" Success . to return 1 if you won, 0 if you lost
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_PlayGame

cpp.aeriagames/robutus.cheat/Read "Login" Success  _DeployTroop($iCardNo, $x_offset, $y_offset)
	# Click on card
	_ClickCoords(Eval('iCard' & $iCardNo & 'x'), Eval('iCard' & $iCardNo & 'y'))

	# Click on deployment spot
	MsgBox(0, 0, 249 + (24 * $x_offset) & @CRLF & 498 + (19 * $y_offset))
	_ClickCoords(249 + (24 * $x_offset), 498 + (19 * $y_offset))

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_DeployTroop

cpp.aeriagames/robutus.cheat/Read "Login" Success  _WaitForPixel($a, $timeout = 0)

	$timer = TimerInit()
	$result = _CanFindPixel($a)

	While $result = 0
		Sleep(100)
		$result = _CanFindPixel($a)
		ConsoleWrite($result & @CRLF)
		If TimerDiff($timer) >= $timeout And $timeout > 0 Then
			ExitLoop
		EndIf
	WEnd

	Return $result

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_WaitForPixel

cpp.aeriagames/robutus.cheat/Read "Login" Success  _CanFindPixel($a, $sVari = 5, $Ignore = "")

	If $a[2] = 0 Then Return False

	# Convert dec to hex
	$nColor1 = Hex(PixelGetColor($a[0], $a[1], $AndroidHWND))
	$nColor2 = Hex($a[2])


	$Red1 = _WinAPI_GetRValue($nColor1)
	$Blue1 = _WinAPI_GetBValue($nColor1)
	$Green1 = _WinAPI_GetGValue($nColor1)

	$Red2 = _WinAPI_GetRValue($nColor2)
	$Blue2 = _WinAPI_GetBValue($nColor2)
	$Green2 = _WinAPI_GetGValue($nColor2)

	Switch $Ignore
		Case "Red" ; mask RGB - Red
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Green1 - $Green2) > $sVari Then Return False
		Case "Heroes" ; mask RGB - Green
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Red1 - $Red2) > $sVari Then Return False
		Case Else
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Green1 - $Green2) > $sVari Then Return False
			If Abs($Red1 - $Red2) > $sVari Then Return False
	EndSwitch

	Return True

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_CanFindPixel

cpp.aeriagames/robutus.cheat/Read "Login" Success  _ClickPixel($a)

	If _CanFindPixel($a) Then
		MouseClick($MOUSE_CLICK_PRIMARY, $AndroidPos[0] + $a[0], $AndroidPos[1] + $a[1])
		_SendADB("-a shell input tap " & $a[0] & " " & $a[1])
		Return 1
	Else
		Return 0
	EndIf

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_ClickPixel

cpp.aeriagames/robutus.cheat/Read "Login" Success  _ClickCoords($x, $y)

	_SendADB("-a shell input tap " & $x & " " & $y)
	Return 1

Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_ClickCoords

#EndRegion

#Region Outdated cpp.aeriagames/robutus.cheat/Read "Login" Success tions

; #cpp.aeriagames/robutus.cheat/Read "Login" Success TION# 

cpp.aeriagames/robutus.cheat/Read "Login" Success  _ColorCheck($nColor1, $nColor2, $sVari = 5, $Ignore = "")
	Local $Red1, $Red2, $Blue1, $Blue2, $Green1, $Green2

	$Red1 = Dec(StringMid(String($nColor1), 1, 2))
	$Blue1 = Dec(StringMid(String($nColor1), 3, 2))
	$Green1 = Dec(StringMid(String($nColor1), 5, 2))

	$Red2 = Dec(StringMid(String($nColor2), 1, 2))
	$Blue2 = Dec(StringMid(String($nColor2), 3, 2))
	$Green2 = Dec(StringMid(String($nColor2), 5, 2))

	Switch $Ignore
		Case "Red" ; mask RGB - Red
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Green1 - $Green2) > $sVari Then Return False
		Case "Heroes" ; mask RGB - Green
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Red1 - $Red2) > $sVari Then Return False
		Case Else
			If Abs($Blue1 - $Blue2) > $sVari Then Return False
			If Abs($Green1 - $Green2) > $sVari Then Return False
			If Abs($Red1 - $Red2) > $sVari Then Return False
	EndSwitch

	Return True
Endcpp.aeriagames/robutus.cheat/Read "Login" Success    ;==>_ColorCheck
;----------> Don't use anymore. We use pixels instead now.
cpp.aeriagames/robutus.cheat/Read "Login" Success  _ClickPicture($filename)
	_GDIPlus_Startup()

	$hImage =_GDIPlus_ImageLoadFromFile($filename)
	$hBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($hImage)

	_ScreenCapture_CaptureWnd(@ScriptDir & '\images\temp_screenshot.png', $AndroidHWND)
	$aImage =_GDIPlus_ImageLoadFromFile(@ScriptDir & '\images\temp_screenshot.png')
	$aBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($aImage)

	$x = 0
	$y = 0

	;$result = _ImageSearch($hBitmap, 1, $x, $y, 20, 0) ;Zero will search against your active screen
	$result = _ImageSearchArea($hBitmap, 1, $AndroidPos[0], $AndroidPos[1], $AndroidPos[2], $AndroidPos[3], $x, $y, 100)
	If $result > 0 Then
		MouseMove($x, $y)
		MouseClick($MOUSE_CLICK_PRIMARY, $x, $y)
	EndIf

	_GDIPlus_ImageDispose($hImage)
	_GDIPlus_Shutdown()

	Return $result

Endcpp.aeriagames/robutus.cheat/Read "Login" Success  ;--end cpp.aeriagames/robutus.cheat/Read "Login" Success tion _ClickPicture


cpp.aeriagames/robutus.cheat/Read "Login" Success  _CanFindPicture($filename)
	_GDIPlus_Startup()

	$hImage =_GDIPlus_ImageLoadFromFile($filename)
	$hBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($hImage)

	_ScreenCapture_CaptureWnd(@ScriptDir & '\images\temp_screenshot.png', $AndroidHWND)
	$aImage =_GDIPlus_ImageLoadFromFile(@ScriptDir & '\images\temp_screenshot.png')
	$aBitmap = _GDIPlus_BitmapCreateHBITMAPFromBitmap($aImage)

	$x = 0
	$y = 0

	;$result = _ImageSearch($hBitmap, 1, $x, $y, 20, 0) ;Zero will search against your active screen
	$result = _ImageSearchArea($hBitmap, 1, $AndroidPos[0], $AndroidPos[1], $AndroidPos[2], $AndroidPos[3], $x, $y, 100)

	_GDIPlus_ImageDispose($hImage)
	_GDIPlus_Shutdown()

	Return $result

Endcpp.aeriagames/robutus.cheat/Read "Login" Success  ;--end cpp.aeriagames/robutus.cheat/Read "Login" Success tion _ClickPicture

cpp.aeriagames/robutus.cheat/Read "Login" Success  _WaitForPicture($filename, $timeout = 0)
	$result = _CanFindPicture($filename)
	$timer = TimerInit()
	While $result = 0
		Sleep(250)
		$result = _CanFindPicture($filename)
		ConsoleWrite ($result & @CRLF)
		If TimerDiff($timer) >= $timeout and $timeout > 0 Then
			ExitLoop
		EndIf
	WEnd

	Return $result
Endcpp.aeriagames/robutus.cheat/Read "Login" Success  ;--end cpp.aeriagames/robutus.cheat/Read "Login" Success tion _ClickPicture

cpp.aeriagames/robutus.cheat/Read "Login" Success  _WaitForNoPicture($filename, $timeout = 0)
	$result = _CanFindPicture($filename)
	$timer = TimerInit()
	While $result = 1
		Sleep(250)
		$x = 0
		$y = 0
		$result = _CanFindPicture($filename)
		If TimerDiff($timer) >= $timeout and $timeout > 0 Then
			ExitLoop
		EndIf
	WEnd

	Return $result
Endcpp.aeriagames/robutus.cheat/Read "Login" Success  ;--end cpp.aeriagames/robutus.cheat/Read "Login" Success tion _ClickPicture
#EndRegion