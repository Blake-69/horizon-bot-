import discord
from discord import app_commands
from discord.ext import commands

class HorizonCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /timetable_claim
    @app_commands.command(name="timetable_claim", description="Claim a timetable slot.")
    @app_commands.describe(teaching_name="Your initials", year="Year group", period="Period", subject="Subject", room="Room")
    async def timetable_claim(self, interaction: discord.Interaction, teaching_name: str, year: str, period: str, subject: str, room: str):
        if 1330284350985470058 not in [role.id for role in interaction.user.roles]:
            await interaction.response.send_message("You do not have permission.", ephemeral=True)
            return

        embed = discord.Embed(title="Timetable Claim", color=0x8b2828)
        embed.add_field(name="Teaching Name", value=teaching_name, inline=False)
        embed.add_field(name="Year", value=year, inline=True)
        embed.add_field(name="Period", value=period, inline=True)
        embed.add_field(name="Subject", value=subject, inline=False)
        embed.add_field(name="Room", value=room, inline=False)
        await interaction.response.send_message(f"{interaction.user.mention}", embed=embed)

    # /timetable
    @app_commands.command(name="timetable", description="View current timetable.")
    async def timetable(self, interaction: discord.Interaction):
        if not any(role.id == 0x11806a for role in interaction.user.roles):
            await interaction.response.send_message("Access denied.", ephemeral=True)
            return

        embed = discord.Embed(title="Timetable", color=0x11806a)
        embed.description = "**Claimed:**\n- Y10 P1: Mr J - Maths - R202\n- Y9 P2: Ms T - History - R101\n\n**Unclaimed:**\n- Y11 P3\n- Y7 P4"
        await interaction.response.send_message(embed=embed)

    # /infract
    @app_commands.command(name="infract", description="Issue a staff infraction.")
    @app_commands.describe(user="Staff to infract", reason="Reason for infraction", type="Type of infraction", demotion_role="Role to demote (optional)")
    async def infract(self, interaction: discord.Interaction, user: discord.Member, reason: str, type: str, demotion_role: str = "N/A"):
        if 1330283312089923674 not in [role.id for role in interaction.user.roles]:
            await interaction.response.send_message("Access denied.", ephemeral=True)
            return

        embed = discord.Embed(title="Infraction Notice", color=0x8b2828)
        embed.add_field(name="Infracted By", value=interaction.user.mention, inline=False)
        embed.add_field(name="Type", value=type, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        if type.lower() == "demotion":
            embed.add_field(name="Demotion Role", value=demotion_role, inline=False)
        await interaction.response.send_message(f"{user.mention}", embed=embed)

    # /promote
    @app_commands.command(name="promote", description="Promote a staff member.")
    @app_commands.describe(user="User to promote", promotion_to="Role or title", reason="Reason for promotion")
    async def promote(self, interaction: discord.Interaction, user: discord.Member, promotion_to: str, reason: str):
        if 1330283312089923674 not in [role.id for role in interaction.user.roles]:
            await interaction.response.send_message("Access denied.", ephemeral=True)
            return

        embed = discord.Embed(title="Promotion Notice", color=0x8b2828)
        embed.add_field(name="Promoted By", value=interaction.user.mention, inline=False)
        embed.add_field(name="Promotion To", value=promotion_to, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text="Please check your direct messages.")
        await interaction.response.send_message(f"{user.mention}", embed=embed)

    # /session_log
    @app_commands.command(name="session_log", description="Log a completed session.")
    @app_commands.describe(user="Staff to log", evidence="Proof of session", session_date="Date of session")
    async def session_log(self, interaction: discord.Interaction, user: discord.Member, evidence: str, session_date: str):
        if 1330284350985470058 not in [role.id for role in interaction.user.roles]:
            await interaction.response.send_message("Access denied.", ephemeral=True)
            return

        embed = discord.Embed(title="Session Log", color=0x8b2828)
        embed.add_field(name="Logged By", value=interaction.user.mention, inline=False)
        embed.add_field(name="Evidence", value=evidence, inline=False)
        embed.add_field(name="Session Date", value=session_date, inline=False)
        embed.set_footer(text="Please check your direct messages.")
        await interaction.response.send_message(f"{user.mention}", embed=embed)

async def setup(bot):
    await bot.add_cog(HorizonCommands(bot))

