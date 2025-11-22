import * as mc from "@minecraft/server";
import * as ui from "@minecraft/server-ui";

const VERSION = "1.0.0";
const SOUND_TURN_PAGE = "item.book.page_turn";
const SOUND_OPTIONS = { pitch: 1.0, volume: 5.0 };

const MENU_MAIN = new ui.ActionFormData();
const MENU_ESSENTIAL = new ui.ActionFormData();

guideBookListeners();
setupStaticMenus();

//most of the menus don't ever change contents so we set them up once at the very start
function setupStaticMenus() {
  //GUIDEBOOK MAIN
  MENU_MAIN.title("§l§f[§cCape Changer§f]");
  MENU_MAIN.body({
    rawtext: [
      { text: "By §3BehaviorPack§r | Version: §q" + VERSION + "\n" },
      { text: "§l§mUnequip your CAPE before use!" },
    ],
  });
  MENU_MAIN.button("Remove Cape");
  MENU_MAIN.button("Common Cape", "textures/capes/icons/Cape_Common");
  MENU_MAIN.button("Yearn Cape", "textures/capes/icons/Yearn_Cape");
  MENU_MAIN.button("Menace Cape", "textures/capes/icons/Menace_Cape");
  MENU_MAIN.button("Home Cape", "textures/capes/icons/Home_Cape");
  MENU_MAIN.button("Mojang Office Cape", "textures/capes/icons/Cape_Office");
  MENU_MAIN.button("MC Experience Cape", "textures/capes/icons/Cape_LBE");
  MENU_MAIN.button("MCC 15th Year Cape", "textures/capes/icons/Mcc_Cape");
  MENU_MAIN.button("15th Anniversary Cape", "textures/capes/icons/15_Cape");
  MENU_MAIN.button("Follower's Cape", "textures/capes/icons/Cape_Tiktok");
  MENU_MAIN.button("Purple Heart Cape", "textures/capes/icons/Cape_Twitch");
  MENU_MAIN.button("Cherry Cape", "textures/capes/icons/Cape_Cherry");
  MENU_MAIN.button("Progress Pride Cape", "textures/capes/icons/Cape_Pride");
  MENU_MAIN.button("One Vanilla", "textures/capes/icons/One_Vanilla_Cape");
  MENU_MAIN.button("Mojang Studios Cape", "textures/capes/icons/Mojang_Studios_Cape");
  MENU_MAIN.button("Founder's Cape", "textures/capes/icons/Founders_Cape");
  MENU_MAIN.button("Extra Fancy Capes", "textures/capes/icons/Sky_Cape");

  //GUIDEBOOK ESSENTIAL
  MENU_ESSENTIAL.title("§lExtra Fancy Capes");
  MENU_ESSENTIAL.body({
    rawtext: [{ text: "Custom Capes from §9Essential §fclient." }],
  });
  MENU_ESSENTIAL.button("Sky Cape", "textures/capes/icons/Sky_Cape");
  MENU_ESSENTIAL.button("Wildflower Cape", "textures/capes/icons/Wildflower_Cape");
  MENU_ESSENTIAL.button("Creaking Cape", "textures/capes/icons/Creaking_Cape");
  MENU_ESSENTIAL.button("Blossom Cape", "textures/capes/icons/Blossom_Cape");
  MENU_ESSENTIAL.button("Booster Cape", "textures/capes/icons/Booster_Cape");
  MENU_ESSENTIAL.button("Sniffer Cape", "textures/capes/icons/Sniffer_Cape");
  MENU_ESSENTIAL.button("Return", "textures/capes/icons/return_icon");
}

function menuMain(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  MENU_MAIN.show(player).then((result) => {
    if (result.canceled) return;
    let response = result.selection;
    switch (response) {
      case 0:
        removeCape(player);
        break;
      case 1:
        commonCape(player);
        break;
      case 2:
        yearnCape(player);
        break;
      case 3:
        menaceCape(player);
        break;
      case 4:
        homeCape(player);
        break;
      case 5:
        capeOffice(player);
        break;
      case 6:
        capeLBE(player);
        break;
      case 7:
        mccCape(player);
        break;
      case 8:
        cape15(player);
        break;
      case 9:
        tiktokCape(player);
        break;
      case 10:
        twitchCape(player);
        break;
      case 11:
        cherryCape(player);
        break;
      case 12:
        prideCape(player);
        break;
      case 13:
        javaBedrockCape(player);
        break;
      case 14:
        mojangstudiosCape(player);
        break;
      case 15:
        foundersCape(player);
        break;
      case 16:
        menuESSENTIAL(player);
        break;
      default:
        break;
    }
  });
}

function removeCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:remove_cape");
}
function commonCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:common_cape");
}
function yearnCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:yearn_cape");
}
function menaceCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:menace_cape");
}
function homeCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:home_cape");
}
function capeOffice(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_office");
}
function capeLBE(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_LBE");
}
function mccCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:mcc_cape");
}
function cape15(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:15_cape");
}
function tiktokCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_tiktok");
}
function twitchCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_twitch");
}
function cherryCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_cherry");
}
function prideCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:cape_pride");
}
function javaBedrockCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:java_bedrock_cape");
}
function mojangstudiosCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:mojangstudios_cape");
}
function foundersCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s capes:founders_cape");
}
function menuESSENTIAL(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  MENU_ESSENTIAL.show(player).then((result) => {
    if (result.canceled) return;

    let response = result.selection;
    switch (response) {
      case 0:
        skyCape(player);
        break;
      case 1:
        wildflowerCape(player);
        break;
      case 2:
        creakingCape(player);
        break;
      case 3:
        blossomCape(player);
        break;
      case 4:
        boosterCape(player);
        break;
      case 5:
        snifferCape(player);
        break;
      case 6:
        menuMain(player);
        break;
      default:
        break;
    }
  });
}
function skyCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:sky_cape");
}
function wildflowerCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:wildflower_cape");
}
function creakingCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:creaking_cape");
}
function blossomCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:blossom_cape");
}
function boosterCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:booster_cape");
}
function snifferCape(player) {
  player.playSound(SOUND_TURN_PAGE, SOUND_OPTIONS);
  player.runCommandAsync("event entity @s customcapes:sniffer_cape");
}

function guideBookListeners() {
  //drop guidebook on player first spawn only
  mc.world.afterEvents.playerSpawn.subscribe((eventData) => {
    if (eventData.player.hasTag("has_cape_changer")) {
    } else {
      mc.world
        .getDimension(eventData.player.dimension.id)
        .spawnItem(new mc.ItemStack("behaviorpack:cape_changer", 1), eventData.player.location);
      eventData.player.addTag("has_cape_changer");
      eventData.player.sendMessage({
        rawtext: [
          { text: "§l§f[§cCape Changer§f]§r Add-On by §9BehaviorPack§r is installed!\n" },
          { text: "§pBe sure to UNEQUIP your cape before use!" },
        ],
      });
    }
  });

  //guidebook activation listener
  mc.world.afterEvents.itemUse.subscribe((eventData) => {
    let player = eventData.source;
    let itemUse = eventData.itemStack;
    if (itemUse === undefined) return;
    if (itemUse.typeId == "behaviorpack:cape_changer") menuMain(player);
  });
}
