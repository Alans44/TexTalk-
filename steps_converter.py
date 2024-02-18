import renderer
import speaker

_steps = r"""Got it, let's break down the solution:

1. **Antiderivative**: 
   - EXP: \int 3x \, dx = \frac{3}{2}x^2 + C
   - EXPL: Integrate \(3x\) with respect to \(x\) to find the antiderivative. The constant of integration \(C\) accounts for any constant shift.

2. **Evaluate at Limits**:
   - EXP: \left[\frac{3}{2}x^2\right]_{0}^{2}
   - EXPL: Substitute \(x = 2\) into the antiderivative and subtract the result when \(x = 0\) to find the definite integral over the interval \([0, 2]\).

3. **Substitute Upper Limit**:
   - EXP: \left[\frac{3}{2}(2)^2\right] - \left[\frac{3}{2}(0)^2\right]
   - EXPL: Calculate the antiderivative at the upper limit.

4. **Calculate**:
   - EXP: \left[\frac{3}{2}(4)\right] - \left[0\right]
   - EXPL: Simplify the expression by evaluating \((2)^2 = 4\) and \((0)^2 = 0\).

5. **Simplify Further**:
   - EXP: \frac{3}{2}(4)
   - EXPL: Multiply \(\frac{3}{2}\) by \(4\).

6. **Final Result**:
   - EXP: 6
   - EXPL: Evaluate the expression to get the final result.

This leads us to the conclusion that the definite integral \(\int_{0}^{2} 3x \, dx\) evaluates to \(6\)."""

def convert(response: str):
    # response = renderer.format_str(response)
    steps = {"EXP": [], "EXPL": []}
    lines = response.split("\n")
    for line in lines:
        if "EXP:" in line:
            steps["EXP"].append(line[line.index("EXP:") + len("EXP:"):].strip())
        elif "EXPL:" in line:
            steps["EXPL"].append(line[line.index("EXPL:") + len("EXPL:"):].strip())
    return steps

def render_steps(steps_dict: dict):
    i = 0
    for exp in steps_dict["EXP"]:
        renderer.render(exp, f"resources/more/.step_{i}.png")
        speaker.tts(steps_dict["EXPL"][i], i)
        print(exp)
        i+=1

if __name__ == "__main__":
    steps_dict = convert(_steps)
    i = 0
    for exp in steps_dict["EXP"]:
        renderer.render(exp, f"resources/more/.step_{i}.png")
        speaker.tts(steps_dict["EXPL"][i], i)
        print(exp)
        i+=1