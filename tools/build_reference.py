#!/usr/bin/env python3
"""Generate the Unreal Engine 5+ reference HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("Overview", "Reference/index.html"),
    ("Getting started", "Reference/GettingStarted/index.html"),
    ("5.5+ features", "Reference/Features/index.html"),
    ("Nanite", "Reference/Nanite/index.html"),
    ("Lumen", "Reference/Lumen/index.html"),
    ("Rendering", "Reference/Rendering/index.html"),
    ("Unreal Insights", "Reference/Insights/index.html"),
    ("Profiling", "Reference/Profiling/index.html"),
    ("Optimization", "Reference/Optimization/index.html"),
    ("Blueprints", "Reference/Blueprints/index.html"),
    ("Blueprint math", "Reference/BlueprintMath/index.html"),
    ("Asset validation", "Reference/Validation/index.html"),
    ("Asset pipeline", "Reference/AssetPipeline/index.html"),
    ("Deployment", "Reference/Deployment/index.html"),
    ("Windows", "Reference/Platforms/Windows/index.html"),
    ("Android", "Reference/Platforms/Android/index.html"),
    ("iOS", "Reference/Platforms/iOS/index.html"),
    ("PlayStation", "Reference/Platforms/PlayStation/index.html"),
    ("Xbox", "Reference/Platforms/Xbox/index.html"),
    ("World building", "Reference/WorldBuilding/index.html"),
    ("Animation", "Reference/Animation/index.html"),
    ("Gameplay", "Reference/Gameplay/index.html"),
    ("Audio & Niagara", "Reference/Audio/index.html"),
    ("Networking", "Reference/Networking/index.html"),
    ("C++ node list", "index.html"),
]


def page(rel, title, lede, body):
    depth = rel.count("/")
    prefix = "../" * depth
    css = prefix + "assets/reference.css"
    home = prefix + "index.html"
    links = []
    for label, href in NAV:
        target = prefix + href
        active = ' class="active"' if href == rel else ""
        links.append(f'<a href="{target}"{active}>{label}</a>')
    nav = "\n".join(links)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Unreal Engine 5+</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<header>
  <a class="home" href="{home}">&larr; Unreal Engine 5+ reference</a>
  <h1>{title}</h1>
  <p>{lede}</p>
</header>
<div class="layout">
<nav>
  <div class="nav-section">UE 5+</div>
  {nav}
</nav>
<main>
{body}
</main>
</div>
<footer>
  Public-engine reference for day-to-day development. Console partner-portal numbers stay in the Sony and Microsoft programs.
  Confirm cvars against the engine version you have open. <a href="{home}">Back to the cheat sheet</a>.
</footer>
</body>
</html>
"""
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(rel)


# ---------- pages ----------

page(
    "Reference/index.html",
    "Unreal Engine 5+ information",
    "One place for features, optimization, profiling, Blueprints, and per-platform settings from 5.5 through 5.8.",
    """
<h2>How to use this</h2>
<div class="card"><div class="body">
<p>The home page still holds the Blueprint-to-C++ node translations. Everything added for Unreal Engine 5.5 and later lives in the folders linked here. Each topic is its own page so you can open it directly or jump from the side list.</p>
<div class="ok">Current public line: 5.5 introduced MegaLights (experimental at the time). 5.6 unified more of the GPU view in Unreal Insights. 5.7 documents Nanite mesh settings and mobile Lumen on high-end Android. 5.8 (June 2026) is the last planned major UE5 release: MegaLights, Iris, Dataflow, Movie Render Graph, Live Link Hub, and Audio Insights are production-ready, and Lumen Lite targets 60 fps on handhelds and lower-end PCs.</div>
</div></div>
<h2>Start here</h2>
<div class="hub">
<a href="GettingStarted/index.html"><strong>Getting started</strong><span>Editor, projects, Blueprints vs C++, first loop</span></a>
<a href="Features/index.html"><strong>5.5+ features</strong><span>What changed in 5.5, 5.6, 5.7, and 5.8</span></a>
<a href="Blueprints/index.html"><strong>Blueprints</strong><span>Graphs, functions, debugging, references</span></a>
<a href="BlueprintMath/index.html"><strong>Blueprint math</strong><span>Expressions, vectors, libraries</span></a>
</div>
<h2>Rendering and measurement</h2>
<div class="hub">
<a href="Nanite/index.html"><strong>Nanite</strong><span>Virtualized geometry and Insights reads</span></a>
<a href="Lumen/index.html"><strong>Lumen</strong><span>GI, reflections, Lumen Lite, mobile</span></a>
<a href="Rendering/index.html"><strong>Rendering</strong><span>VSM, MegaLights, Substrate, TSR</span></a>
<a href="Insights/index.html"><strong>Unreal Insights</strong><span>Traces aimed at Nanite and Lumen</span></a>
<a href="Profiling/index.html"><strong>Profiling</strong><span>stat, ProfileGPU, memory, hitches</span></a>
<a href="Optimization/index.html"><strong>Optimization</strong><span>Budgets and what to change first</span></a>
</div>
<h2>Content and shipping</h2>
<div class="hub">
<a href="Validation/index.html"><strong>Asset validation</strong><span>Checkers on Blueprints and assets</span></a>
<a href="AssetPipeline/index.html"><strong>Asset pipeline</strong><span>Interchange, cook, streaming</span></a>
<a href="Deployment/index.html"><strong>Deployment</strong><span>Cook, package, iterate on device</span></a>
<a href="Platforms/Windows/index.html"><strong>Windows</strong><span>DX12, SM6, scalability</span></a>
<a href="Platforms/Android/index.html"><strong>Android</strong><span>Vulkan, device profiles, Lumen</span></a>
<a href="Platforms/iOS/index.html"><strong>iOS</strong><span>Metal, scale factor, no Lumen</span></a>
<a href="Platforms/PlayStation/index.html"><strong>PlayStation</strong><span>UE-side settings, public only</span></a>
<a href="Platforms/Xbox/index.html"><strong>Xbox</strong><span>UE-side settings, public only</span></a>
</div>
<h2>Gameplay systems</h2>
<div class="hub">
<a href="WorldBuilding/index.html"><strong>World building</strong><span>World Partition, PCG, terrain</span></a>
<a href="Animation/index.html"><strong>Animation</strong><span>Control Rig, retarget, Sequencer</span></a>
<a href="Gameplay/index.html"><strong>Gameplay</strong><span>Enhanced Input, GAS, State Tree</span></a>
<a href="Audio/index.html"><strong>Audio and Niagara</strong><span>MetaSounds, VFX, Audio Insights</span></a>
<a href="Networking/index.html"><strong>Networking</strong><span>Replication, Iris, listen servers</span></a>
</div>
""",
)

page(
    "Reference/GettingStarted/index.html",
    "Getting started",
    "What a new programmer should know before touching Nanite settings or device profiles.",
    """
<h2>Project shape</h2>
<div class="card"><h3>Create the project for the platforms you will ship</h3><div class="body">
<ul>
<li>Pick a template that matches the game (first person, third person, blank). Blank is easier to reason about while learning.</li>
<li>Target the highest platform first only if you will actually ship it. A mobile-first project should start with the Mobile renderer, not a desktop Lumen scene you later strip.</li>
<li>Enable only the plugins you use. Extra plugins add cook time, shader permutations, and Blueprint nodes you do not need.</li>
<li>Keep C++ and Blueprint in the same module layout from day one: gameplay in a game module, reusable math and validators in a separate editor or runtime module.</li>
</ul>
</div></div>
<div class="card"><h3>Blueprints and C++ together</h3><div class="body">
<p>Blueprints are the default gameplay graph. C++ is for systems you tick often, data you want the compiler to check, and anything shared by many Blueprints.</p>
<ul>
<li>Expose design knobs with <code>UPROPERTY(EditAnywhere, BlueprintReadWrite)</code> and actions with <code>UFUNCTION(BlueprintCallable)</code>.</li>
<li>Use <code>BlueprintImplementableEvent</code> when C++ should call a graph the designer fills in, and <code>BlueprintNativeEvent</code> when C++ has a default the graph can override.</li>
<li>The home page of this site maps common Blueprint nodes to the C++ calls they wrap.</li>
</ul>
</div></div>
<div class="card"><h3>Frame of the editor</h3><div class="body">
<ul>
<li><strong>Content Browser</strong> is the asset database. Folders are not classes. Name assets by type prefix your team agrees on (<code>BP_</code>, <code>M_</code>, <code>T_</code>, <code>SM_</code>, <code>NS_</code>).</li>
<li><strong>Outliner</strong> is the actors in the open level. World Partition levels stream cells instead of one giant actor list.</li>
<li><strong>Details</strong> is per-selection properties. Class defaults live on the Blueprint editor, not on a placed instance, unless you override them.</li>
<li><strong>Output Log</strong> is where <code>Print String</code> and <code>UE_LOG</code> land. Read it before assuming a node did not fire.</li>
</ul>
</div></div>
<h2>First habits</h2>
<div class="card"><h3>References</h3><div class="body">
<ul>
<li>A hard reference (object pin, defaulted asset) loads that asset whenever the referencer loads.</li>
<li>A soft reference (<code>TSoftObjectPtr</code>, Soft Object Path) records the path and loads on demand. Use it for UI, levels, and large meshes a menu should not pull in.</li>
<li>Casting to a Blueprint class hard-references that class. Cast to a C++ parent or a Blueprint interface when many types share a behavior.</li>
</ul>
</div></div>
<div class="card"><h3>Construction Script, BeginPlay, Tick</h3><div class="body">
<ul>
<li><strong>Construction Script</strong> runs in the editor when you move the actor or change a property. Keep it deterministic and cheap. Do not spawn gameplay that should exist only at runtime.</li>
<li><strong>BeginPlay</strong> runs when the actor starts playing. Cache components here.</li>
<li><strong>Tick</strong> runs every frame. New programmers put too much here. Prefer timers, overlap events, and Enhanced Input.</li>
</ul>
</div></div>
<div class="card"><h3>Where settings live</h3><div class="body">
<table>
<tr><th>Place</th><th>Use it for</th></tr>
<tr><td>Project Settings</td><td>Engine features: Nanite, Lumen, mobile HDR, maps to cook, platform SDK</td></tr>
<tr><td>Config/DefaultEngine.ini and platform Engine.ini</td><td>Checked-in cvars and system settings</td></tr>
<tr><td>Config/DefaultDeviceProfiles.ini</td><td>Per-device or per-bucket console variables</td></tr>
<tr><td>Config/DefaultScalability.ini</td><td>Low / medium / high / epic / cinematic groups</td></tr>
<tr><td>Post Process Volume</td><td>Per-level look: exposure, GI method, reflection method</td></tr>
<tr><td>Developer console (`)</td><td>Experiments. Promote the ones you keep into config.</td></tr>
</table>
</div></div>
""",
)

page(
    "Reference/Features/index.html",
    "Unreal Engine 5.5 and later",
    "Nuances that matter when you move a project from 5.4 onto 5.5, 5.6, 5.7, or 5.8.",
    """
<h2>5.5</h2>
<div class="card"><h3>What to learn</h3><div class="body">
<ul>
<li><strong>MegaLights</strong> arrived as the many-shadowed-lights path. In 5.5 it was new and easy to over-trust. Treat early captures as experiments; 5.8 marks it production-ready.</li>
<li><strong>Nanite</strong> mesh settings grew: fallback meshes, displacement, edge-length limits for deforming meshes, and explicit tangents. The 5.7 Blueprint struct <em>Mesh Nanite Settings</em> exposes those fields.</li>
<li><strong>Lumen on DirectX 11 / Shader Model 5</strong> regressed for some 5.5.x builds. Software Lumen on Windows is reliable on DX12 with Shader Model 6. Vulkan SM5 could still run it when DX11 could not.</li>
<li><strong>Ray tracing</strong> has been a plugin since 5.4. Hardware Lumen and path tracing need that plugin, DX12, and a GPU that supports it. Do not expect the old project-settings checkbox layout.</li>
<li><strong>Path tracer</strong> gained denoising work (including NFOR discussions in 5.5 comparisons). It is a ground-truth tool, not a gameplay GI solution.</li>
<li>Mobile device profiles needed newer GPU entries. If a new Android phone falls through to a low bucket, check <code>DefaultDeviceProfiles.ini</code> before blaming the renderer.</li>
</ul>
</div></div>
<h2>5.6</h2>
<div class="card"><h3>What to learn</h3><div class="body">
<ul>
<li><strong>Unreal Insights GPU view</strong> lines up more closely with <code>ProfileGPU</code>. From 5.6, read Graphics and Compute as separate tracks. Most of Lumen's gather and reflections sit on the compute side.</li>
<li><strong>Material editor</strong> updates live in the viewport as you scrub parameters, adds a Convert node, better node search, reroute creation, and custom texture channel names.</li>
<li><strong>Modeling Mode</strong> tools (XForm, Pattern, Deform, PolyGroup, subdivision) are part of everyday blockout, not a side plugin you ignore.</li>
</ul>
</div></div>
<h2>5.7</h2>
<div class="card"><h3>What to learn</h3><div class="body">
<ul>
<li>Nanite settings are a first-class struct you can break in Blueprints: enabled, lerp UVs, shape preservation, fallback generation, max edge length, displacement UV channel, voxel opacity.</li>
<li>Public mobile Lumen docs describe an experimental desktop renderer on high-end Android Vulkan SM5 devices. iOS, tvOS, and iPadOS do not run Lumen.</li>
<li>Keep a non-Lumen lighting tier (static or stationary lightmaps, reflection captures) for the phones that miss the SM5 profile.</li>
</ul>
</div></div>
<h2>5.8</h2>
<div class="card"><h3>Production-ready in this release</h3><div class="body">
<table>
<tr><th>Feature</th><th>Practical meaning</th></tr>
<tr><td>MegaLights</td><td>Many dynamic shadowed lights, aimed at 60 fps on current-gen consoles</td></tr>
<tr><td>Lumen Lite</td><td>Faster GI than Lumen High Quality for handhelds and lower-end PCs</td></tr>
<tr><td>Iris</td><td>Newer replication system you can adopt instead of only the classic net driver</td></tr>
<tr><td>Dataflow</td><td>Node graphs for Chaos cloth and destruction authoring</td></tr>
<tr><td>Movie Render Graph</td><td>Graph-based cinematic renders and layers</td></tr>
<tr><td>Live Link Hub</td><td>One place for performance-capture devices and recording</td></tr>
<tr><td>Audio Insights</td><td>Profile MetaSounds and audio in the Insights toolchain</td></tr>
</table>
<ul>
<li><strong>Mesh Terrain</strong> is experimental mesh-based landscape (caves, overhangs), separate from heightfield Landscape.</li>
<li><strong>Procedural Vegetation Editor</strong> builds Nanite-ready plants that can take wind.</li>
<li><strong>Toon Shader</strong> and <strong>Fog Screen Space Scattering</strong> are look features, not free. Profile them like any other pass.</li>
<li><strong>MetaHuman</strong> crowds, markerless single-camera capture, and broader Mesh to MetaHuman.</li>
<li><strong>MCP plugin</strong> (experimental) lets an external model call engine tools. It is an editor integration, not a gameplay feature.</li>
<li>Android cooks skip more unchanged work, SDK setup is more automated, and the Unreal Engine Remote app previews mobile input from the editor.</li>
<li>Shader dedup and PSO precache are a shipping concern. Hitching on first-run materials is often a PSO miss, not a Blueprint bug.</li>
</ul>
<div class="callout">Epic has said 5.8 is the last planned major UE5 release, with room for a 5.9 if they need one. Pin your project to a hotfix (5.8.1 and later) and read that hotfix's upgrade notes before copying config from an older engine.</div>
</div></div>
""",
)

page(
    "Reference/Nanite/index.html",
    "Nanite",
    "Virtualized geometry: when to enable it, how it spends the frame, and how Insights shows that cost.",
    """
<h2>What it is</h2>
<div class="card"><h3>Cluster LODs, not classic screen-size LODs</h3><div class="body">
<p>Nanite stores a mesh as clusters and picks how much detail to draw per cluster from the pixels it covers. You author a high triangle mesh, enable Nanite on the static mesh, and the renderer keeps a budget of pixels per edge instead of swapping whole LOD meshes.</p>
<ul>
<li>Project switch: Project Settings → Engine → Rendering → Nanite. The mesh also has its own Nanite flag. Both must allow it.</li>
<li>It wants Shader Model 6 and a desktop renderer (DirectX 12 on Windows, the high-end Vulkan path where you explicitly opt in).</li>
<li>It does not replace materials, textures, or animation. A dense mesh with a unique heavy material per rock is still expensive.</li>
<li>Fallback meshes exist so platforms and passes that cannot use Nanite still have something to draw. Set fallback triangle percent on purpose; the default is a guess.</li>
</ul>
</div></div>
<div class="card"><h3>5.5+ mesh settings worth knowing</h3><div class="body">
<ul>
<li><strong>Max edge length factor</strong> stops clusters from simplifying so far that a mesh deformed by World Position Offset or a spline looks broken. Leave it at 0 unless you see that bug.</li>
<li><strong>Lerp UVs</strong> should stay on for normal texture coordinates. Turn it off only when a UV channel stores indexes or other data that must not interpolate. If you disable it, Nanite no longer accounts for that UV error when it picks a LOD.</li>
<li><strong>Explicit tangents</strong> cost memory. Use them when implicit tangents shade wrong (mirrors, hard authored seams).</li>
<li><strong>Displacement</strong> samples a height map on a UV channel and can use voxel methods (opacity, NDF). Displacement is a content choice with a build cost, not a checkbox you enable on every mesh.</li>
<li><strong>Preserve area / shape preservation</strong> matters for foliage and thin geo that disappears when simplified.</li>
<li>Skeletal and skinned Nanite, assemblies, and spline meshes have matured across 5.4–5.8. Confirm the support level in your build before you convert a character pipeline.</li>
</ul>
</div></div>
<h2>Authoring rules</h2>
<div class="card"><h3>Enable it when the win is real</h3><div class="body">
<ul>
<li>Good fits: kitbash environments, rocks, dense modular sets, hero props with millions of triangles, Nanite vegetation from the Procedural Vegetation Editor (5.8).</li>
<li>Poor fits: a 300-triangle crate, UI meshes, anything that is fully translucent, or a mesh whose material is masked across most of the screen. Masked Nanite overdraw shows up in the Nanite overdraw view.</li>
<li>World Position Offset that moves vertices a lot fights the cluster LOD. Use the edge-length control, or keep that mesh on classic LODs.</li>
<li>Instancing still matters. A thousand unique Nanite components cost more CPU scene setup than instanced copies.</li>
</ul>
</div></div>
<h2>Read it in Insights and the viewport</h2>
<div class="card"><h3>Views and stats</h3><div class="body">
<ul>
<li>Viewport: Lit → Nanite Visualization. Use <strong>Triangles</strong>, <strong>Clusters</strong>, <strong>Overdraw</strong>, <strong>Material ID</strong>, and <strong>Raster Bins</strong>.</li>
<li>Material ID and raster bins tell you whether the cost is geometry or too many programmable raster materials. Lots of tiny triangles with few materials is the cheap case. Lots of materials is the expensive case.</li>
<li>Console: <code>stat nanite</code> for instances, triangles, and clusters. <code>nanitestats</code> prints a deeper dump.</li>
<li><code>ProfileGPU</code> and the Insights GPU track show Nanite vis-buffer and base-pass time. Compare a camera that sees the dense set with one that does not.</li>
<li>Streaming: if Nanite pops or stalls, look at the streaming pool and IO, not only the raster pass. <code>stat streaming</code> still applies.</li>
</ul>
<pre>stat nanite
r.Nanite.MaxPixelsPerEdge 1
ProfileGPU</pre>
<p class="note">Lower pixels-per-edge keeps more detail and costs more. Change it in a device profile per platform, not as a one-off in a packaged shipping build you forget about.</p>
</div></div>
<div class="card"><h3>Insights workflow for a Nanite scene</h3><div class="body">
<ol>
<li>Development build, <code>r.GPUStatsEnabled 1</code>.</li>
<li><code>Trace.File default,gpu,frame,bookmark</code> or launch with <code>-trace=cpu,gpu,frame,bookmark</code>.</li>
<li>Move the camera through the heavy area. Drop a bookmark (<code>Trace.Bookmark</code> or the Insights bookmark) at the worst frame.</li>
<li>In Insights, open the GPU track and find Nanite raster and material bins. If Compute is idle and Graphics Nanite is tall, you are raster-bound. If bins explode, you are material-bound.</li>
<li>Cross-check with the Nanite Overdraw view on that same camera.</li>
</ol>
</div></div>
""",
)

page(
    "Reference/Lumen/index.html",
    "Lumen",
    "Dynamic global illumination and reflections, including Lumen Lite and the Android limits.",
    """
<h2>How the frame is split</h2>
<div class="card"><h3>Three costs, not one toggle</h3><div class="body">
<p>Lumen is dynamic GI and reflections. In a GPU trace the time usually lands in three places:</p>
<ul>
<li><strong>Lumen Scene Lighting</strong> updates the surface cache (cards) that rays hit.</li>
<li><strong>Lumen Screen Probe Gather</strong> is the diffuse final gather. It often dominates.</li>
<li><strong>Lumen Reflections</strong> traces what the screen can see, then falls back to the Lumen scene.</li>
</ul>
<p>Software traces use signed distance fields and the surface cache. Hardware traces use the ray tracing plugin and Shader Model 6. Hardware is not automatically faster; it is more accurate on thin and overlapping geometry. Measure both.</p>
</div></div>
<div class="card"><h3>Project and volume settings</h3><div class="body">
<ul>
<li>Project Settings → Rendering: Dynamic Global Illumination Method = Lumen, Reflection Method = Lumen. Generate mesh distance fields if you use software traces.</li>
<li>Post Process Volume (infinite extent) can override GI and reflection method per level so a menu can be unlit while the game uses Lumen.</li>
<li>Scalability groups <code>sg.GlobalIlluminationQuality</code> and <code>sg.ReflectionQuality</code> are the shipping knobs. Put them in <code>DefaultScalability.ini</code>, then override per device profile.</li>
<li>Software Lumen on Windows: DirectX 12 and Shader Model 6. 5.5.x left DX11 / SM5 Lumen broken for many projects.</li>
<li>Hardware Lumen: enable the ray tracing plugin, <code>r.RayTracing 1</code>, and a GPU that supports it. <code>r.Lumen.HardwareRayTracing 1</code> selects that path.</li>
</ul>
<pre>r.Lumen.DiffuseIndirect.Allow 1
r.Lumen.Reflections.Allow 1
r.Lumen.HardwareRayTracing 0
stat lumen
stat gpu</pre>
</div></div>
<h2>5.5 through 5.8</h2>
<div class="card"><h3>Quality modes</h3><div class="body">
<ul>
<li><strong>Lumen High</strong> is the desktop and current-gen look. Profile screen probes first when you are over budget.</li>
<li><strong>Lumen Lite</strong> (5.8) is the faster mode Epic describes as up to twice as fast as high quality, aimed at 60 fps on handhelds and lower-end PCs. Use it as a platform setting, not as a global downgrade of your hero PC target.</li>
<li>Short-range AO and skylight leaks are content issues as often as they are cvars: large two-sided meshes, missing distance fields, and foliage cards confuse the surface cache.</li>
<li>Emissive meshes light the Lumen scene. A huge emissive shader is a light. Budget it.</li>
<li>MegaLights (production-ready in 5.8) handles many direct shadowed lights. Lumen still does the bounce. They stack. Profile them separately.</li>
</ul>
</div></div>
<div class="card"><h3>Mobile</h3><div class="body">
<ul>
<li>iOS, iPadOS, and tvOS: Lumen does not run. Use static or stationary lightmaps, reflection captures, and a single per-pixel directional light if you need the sun.</li>
<li>Android: experimental Lumen needs the desktop renderer on Vulkan Shader Model 5 profiles such as <code>Android_Vulkan_SM5</code>, on high-end devices only. Turn off <code>r.Android.DisableVulkanSupport</code> and <code>r.Android.DisableVulkanSM5Support</code>, and review <code>r.RayTracing.RequireSM6</code> only if you are following Epic's mobile hardware-RT notes.</li>
<li>Everyone else on Android stays on the mobile lighting tiers (LDR, basic static, full HDR, HDR plus one sun).</li>
</ul>
<div class="callout">Do not cook a Lumen-only lighting setup and discover on device that the phone picked <code>Android_Low</code>. Match profiles in Device Profiles before you light the level.</div>
</div></div>
<div class="card"><h3>Insights for Lumen</h3><div class="body">
<ol>
<li><code>Trace.Start gpu,rhi,frame,bookmark</code> on a Development build.</li>
<li>Open the GPU / Compute track (5.6 and later). Find Screen Probe Gather, Reflections, and Scene Lighting.</li>
<li><code>ProfileGPU</code> (Ctrl+Shift+,) for one frame when a single marker is ambiguous.</li>
<li>If Scene Lighting is the spike, the surface cache is rebuilding (camera cuts, lots of new cards, WPO). If Gather is the spike, lower GI scalability or trace distance. If Reflections is the spike, cut roughness threshold and screen traces before you turn reflections off.</li>
</ol>
</div></div>
""",
)

page(
    "Reference/Rendering/index.html",
    "Rendering features",
    "Virtual Shadow Maps, MegaLights, Substrate, TSR, and the toon and fog additions in 5.8.",
    """
<h2>Shadows and lights</h2>
<div class="card"><h3>Virtual Shadow Maps</h3><div class="body">
<p>VSM is the shadow map system that pairs with Nanite. Pages cache and only redraw what moved. A fully dynamic world (every mesh using World Position Offset, every light moving) invalidates that cache and the cost returns.</p>
<ul>
<li><code>stat virtualshadowmaps</code> shows page pool and cache behavior.</li>
<li>Non-Nanite geometry still casts, but the usual win assumes Nanite casters.</li>
<li>On mobile forward renderers, classic cascaded shadow maps for one directional light are the supported path. Do not expect VSM there.</li>
</ul>
</div></div>
<div class="card"><h3>MegaLights</h3><div class="body">
<p>MegaLights makes large numbers of dynamic shadowed lights practical. It shipped experimental in 5.5 and is production-ready in 5.8, with a stated goal of 60 fps on current-generation consoles.</p>
<ul>
<li>Use it when the design is many local lights (street, interior practicals, spells), not to replace a single sun.</li>
<li>5.5 captures showed mixed artifact results. Re-test on 5.8 before you lock art direction to it.</li>
<li>Separate its GPU time from Lumen. Direct lighting and bounce lighting fail for different reasons.</li>
</ul>
</div></div>
<h2>Materials and upscalers</h2>
<div class="card"><h3>Substrate</h3><div class="body">
<p>Substrate (the material shading model that replaced the older Strata experiment) authorizes layered slabs: clear coat, cloth fuzz, subsurface, eyes. Enable it only when the project needs that shading. It changes material permutations and shader compile times.</p>
<p>5.6 material-editor quality-of-life (live preview, Convert node, better search) applies whether or not Substrate is on.</p>
</div></div>
<div class="card"><h3>TSR and anti-aliasing</h3><div class="body">
<ul>
<li>Temporal Super Resolution is the default upscaler. Resolution scale at 66% or so is a normal shipping choice on consoles and PC, not a debug hack.</li>
<li>Plugins can add DLSS, FSR, or XeSS. Pick one upscaler per platform build.</li>
<li>Mobile often uses FXAA or MSAA depending on HDR and the renderer. Temporal AA is expensive on low tiers.</li>
<li>5.8 adds a Toon shader path and Fog Screen Space Scattering. Both are extra passes. Check them with <code>stat gpu</code> before you leave them on for mobile.</li>
</ul>
</div></div>
<div class="card"><h3>Path tracer</h3><div class="body">
<p>The path tracer is for ground truth and Movie Render Graph cinematics, not for the game view. It needs hardware ray tracing. Compare Lumen against it when art says the bounce looks wrong, then fix content or Lumen settings rather than shipping the path tracer.</p>
</div></div>
""",
)

page(
    "Reference/Insights/index.html",
    "Unreal Insights",
    "How to capture a trace and read Nanite, Lumen, CPU, and loading in one session.",
    """
<h2>Start a capture</h2>
<div class="card"><h3>Editor and packaged game</h3><div class="body">
<p>UnrealInsights.exe lives under <code>Engine/Binaries/Win64</code>. Start it first if you want a live connection, or write a <code>.utrace</code> and open it later.</p>
<pre>UnrealEditor.exe YourProject.uproject -trace=cpu,gpu,frame,bookmark,log -statnamedevents

YourGame.exe -trace=cpu,gpu,frame,bookmark,counters -tracehost=127.0.0.1

Trace.Start cpu,gpu,frame,bookmark
Trace.Bookmark NaniteStreet
Trace.Stop

Trace.File default,gpu</pre>
<ul>
<li><code>cpu</code> plus <code>-statnamedevents</code> names scopes that would otherwise show up as anonymous.</li>
<li><code>gpu</code> is required before any Nanite or Lumen GPU conclusion. Set <code>r.GPUStatsEnabled 1</code>.</li>
<li><code>bookmark</code> and <code>region</code> marks let you compare a room before and after a cvar.</li>
<li><code>file,loadtime,assetloadtime</code> explain hitches when a soft reference resolves.</li>
<li><code>counters</code> adds the stat counters Insights can graph.</li>
<li>Channels <code>rhicommands</code> and <code>rendercommands</code> are heavy. Use them for a short capture when the GPU track is not enough.</li>
</ul>
</div></div>
<div class="card"><h3>Regions</h3><div class="body">
<p>Trace regions limit a comparison to a few seconds inside a long file. Console: <code>Trace.RegionBegin Street</code> and <code>Trace.RegionEnd Street</code>. Blueprints can call the region start and end nodes. C++ has <code>TRACE_BEGIN_REGION</code> / <code>TRACE_END_REGION</code>.</p>
<p>Insights can export timer stats for a region to CSV so you can diff two cvars without eyeballing the graph. On 5.6 and later, export the GPU thread when the question is Lumen or Nanite.</p>
</div></div>
<h2>What to look at</h2>
<div class="card"><h3>Nanite</h3><div class="body">
<ul>
<li>GPU Graphics track: vis buffer, raster, material classify. A wide raster block with healthy culling means the resolution or pixel-per-edge target is the knob.</li>
<li>Many programmable raster bins means masked or WPO materials fell off the fast path. Check Nanite Visualization → Material ID.</li>
<li>CPU game thread spikes next to Nanite are usually instance culling, streaming requests, or too many primitive components, not the rasterizer.</li>
</ul>
</div></div>
<div class="card"><h3>Lumen</h3><div class="body">
<ul>
<li>Read the Compute track for Screen Probe Gather, reflections, and radiosity probes.</li>
<li>A spike only on the frame you cut the camera is surface-cache invalidation. A spike every frame is your steady budget.</li>
<li>Compare Lumen High and Lumen Lite (5.8) with two regions in the same trace.</li>
</ul>
</div></div>
<div class="card"><h3>Other 5.8 views</h3><div class="body">
<ul>
<li><strong>Audio Insights</strong> is production-ready in 5.8. Use it when MetaSounds hitch or voice counts climb. Do not guess from the game thread alone.</li>
<li>Memory traces and <code>memreport</code> answer a different question than timing traces. Capture both if the device is closing the app.</li>
<li>Network traces belong with Iris or the classic replication insights, not in the GPU file.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Profiling/index.html",
    "Profiling",
    "A repeatable order of checks before you change a cvar.",
    """
<h2>In the running game</h2>
<div class="card"><h3>First three commands</h3><div class="body">
<pre>stat unit
stat unitgraph
stat gpu</pre>
<p><code>stat unit</code> splits Frame, Game, Draw, GPU, and RHIT. The largest number is the bound you work on. If Game is 20 ms and GPU is 8 ms, Nanite and Lumen are not the problem.</p>
<table>
<tr><th>Command</th><th>Question it answers</th></tr>
<tr><td><code>stat fps</code></td><td>Is the frame time even the bug you think it is?</td></tr>
<tr><td><code>stat game</code></td><td>Which tick group owns the game thread?</td></tr>
<tr><td><code>stat scenerendering</code></td><td>Draw calls and primitive counts</td></tr>
<tr><td><code>stat nanite</code></td><td>Clusters, triangles, instances</td></tr>
<tr><td><code>stat lumen</code></td><td>Lumen update and probe counters</td></tr>
<tr><td><code>stat virtualshadowmaps</code></td><td>VSM cache and page pool</td></tr>
<tr><td><code>stat streaming</code></td><td>Texture and geometry pools</td></tr>
<tr><td><code>stat memory</code></td><td>Coarse memory categories</td></tr>
<tr><td><code>stat hitches</code></td><td>Frames over the hitch threshold</td></tr>
<tr><td><code>ProfileGPU</code></td><td>One-frame hierarchical GPU dump</td></tr>
</table>
</div></div>
<div class="card"><h3>Viewport view modes</h3><div class="body">
<ul>
<li>Shader Complexity (Alt+8) for materials. On mobile preview this is the first art review.</li>
<li>Quad Overdraw for transparency and masked stacks.</li>
<li>Nanite Overdraw and Material ID.</li>
<li>Light Complexity where MegaLights is off and you still have many forward lights.</li>
<li>LOD Coloration when a mesh is not Nanite and the wrong LOD is stuck.</li>
</ul>
</div></div>
<h2>Deeper captures</h2>
<div class="card"><h3>When stat unit is not enough</h3><div class="body">
<ul>
<li><strong>Unreal Insights</strong> for multi-frame CPU and GPU. See the Insights page.</li>
<li><strong>CSV profiler</strong> and <code>csvprofile</code> for automated runs you can diff in spreadsheets.</li>
<li><strong>memreport -full</strong> writes a report under <code>Saved/Profiling/MemReports</code>.</li>
<li><strong>obj list</strong> shows which UObject classes are resident. A leaked UI widget shows up here.</li>
<li>Platform GPU captures (PIX on Windows and Xbox dev kits, RenderDoc where the RHI allows it, the vendor capture on Android/iOS) explain a single pass Insights only names.</li>
</ul>
<div class="ok">Profile Development builds on the target device. Editor frame time includes selection, thumbnails, and uncooked assets. A 60 fps editor number is not a shipping number.</div>
</div></div>
<div class="card"><h3>Hitch checklist</h3><div class="body">
<ol>
<li>PSO compilation on first sight of a material. Fix with precache, not with a smaller texture.</li>
<li>Synchronous load of a hard-referenced asset. Move it to a soft reference or an async load.</li>
<li>Garbage collection. Shorten the set of live UObjects; do not hide the hitch with a longer time limit only.</li>
<li>Shader compile in editor. That one does not exist in a cooked game.</li>
<li>Nanite or texture streaming catch-up after a camera teleport. Warm the stream or cut through a load screen.</li>
</ol>
</div></div>
""",
)

page(
    "Reference/Optimization/index.html",
    "Optimization",
    "Order of work for a new programmer: measure, then change one thing.",
    """
<h2>Budgets</h2>
<div class="card"><h3>Pick a frame time before you pick a feature</h3><div class="body">
<table>
<tr><th>Target</th><th>Frame time</th><th>Typical rendering path</th></tr>
<tr><td>Cinematic / 30 fps hero</td><td>33 ms</td><td>Nanite, Lumen High, VSM, MegaLights, TSR</td></tr>
<tr><td>60 fps current-gen and high PC</td><td>16.6 ms</td><td>Same features, lower resolution scale, Lumen and shadow scalability at High not Cinematic</td></tr>
<tr><td>60 fps handheld / low PC (5.8)</td><td>16.6 ms</td><td>Lumen Lite or baked lighting, limited Nanite, aggressive resolution scale</td></tr>
<tr><td>Mobile broad</td><td>33 ms or 16.6 ms</td><td>Mobile HDR tiers, no Lumen on iOS, static lights, ASTC, content scale factor</td></tr>
</table>
<p>Leave at least a few milliseconds for gameplay, audio, and the platform compositor. A GPU that fills the whole 16.6 ms will hitch the moment a particle overlaps the screen.</p>
</div></div>
<h2>CPU</h2>
<div class="card"><h3>Blueprint and tick</h3><div class="body">
<ul>
<li>Turn tick off on actors that only react to overlaps, hits, or input.</li>
<li>Do not <code>Get All Actors of Class</code> on tick. Cache the reference, use an interface, or register with a subsystem.</li>
<li>Heavy Blueprint math on tick belongs in C++ or a timer. The node graph has a real call cost.</li>
<li>Animation: update rate optimization and anim budgets before you rewrite the graph.</li>
<li>Chaos: simplify collision. Complex as simple is a shipping foot-gun.</li>
</ul>
</div></div>
<h2>GPU</h2>
<div class="card"><h3>Change in this order</h3><div class="body">
<ol>
<li>Resolution scale and TSR, because it multiplies every later pass.</li>
<li>Shadowed light count, VSM invalidation, then MegaLights if you are on 5.8 and the design needs the lights.</li>
<li>Lumen scalability, then Lumen Lite on the platforms that need it.</li>
<li>Nanite pixels per edge and masked/WPO materials.</li>
<li>Overdraw: particles, translucent fog, decals.</li>
<li>Texture streaming pool size per device profile so you do not blur or thrash.</li>
</ol>
</div></div>
<div class="card"><h3>Content rules that beat cvars</h3><div class="body">
<ul>
<li>Unique materials on every mesh defeat instancing and Nanite bins.</li>
<li>Max texture size in the texture LOD group per memory bucket (tiny phones do not need 4K world textures).</li>
<li>HLOD and World Partition cell sizes so a streaming cell is not the whole country.</li>
<li>One stationary directional light on mobile. Extra dynamic lights belong on the high Android profile only.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Blueprints/index.html",
    "Blueprints",
    "How to work in the graph without painting yourself into a corner.",
    """
<h2>Graph types</h2>
<div class="card"><h3>Event graph, functions, macros</h3><div class="body">
<ul>
<li><strong>Event graph</strong> holds events (BeginPlay, overlaps, input). It can store latent nodes such as Delay and timelines.</li>
<li><strong>Functions</strong> are called and return. They cannot contain latent nodes. Mark a function <em>Pure</em> when it only computes and must not change state. Pure nodes run again every time they are wired, so an expensive pure function can execute more often than you think.</li>
<li><strong>Macros</strong> paste their graph at each call. They can have exec pins and branches. They do not exist as a separate call at runtime, and they cannot be overridden in a child.</li>
<li><strong>Collapsed graphs</strong> are organization. They do not change lifetime or replication.</li>
<li><strong>Event dispatchers</strong> let an actor shout without knowing who listens. Prefer them over casting to a specific widget.</li>
<li><strong>Interfaces</strong> (<code>BPI_</code>) let you call a function on any implementer without a hard class reference.</li>
</ul>
</div></div>
<div class="card"><h3>Execution</h3><div class="body">
<ul>
<li>White exec wires are order. Data wires are values. A node does not run because its data input changed; something must execute it, unless it is pure and connected to a node that is executing.</li>
<li>Sequence is explicit order. Do not rely on the order of branches you did not wire.</li>
<li>Local variables exist only during a function. Use them to avoid computing the same trace twice.</li>
<li>Validate objects with Is Valid before you use a pin that might be empty. The home-page C++ sheet shows both the pointer check and <code>UKismetSystemLibrary::IsValid</code>.</li>
</ul>
</div></div>
<h2>Working habits</h2>
<div class="card"><h3>Debugging</h3><div class="body">
<ul>
<li>Place a breakpoint on a node. Play in the editor. The graph pauses and shows pin values.</li>
<li>Enable <em>Show inherited variables</em> and watch the parent class. A child that does nothing often forgot to call the parent.</li>
<li>Print String goes to the screen and the Output Log. Remove it before you profile; the widget has a cost.</li>
<li>The compiler tab is the source of truth for errors. A Blueprint that compiles with warnings about unused pins is fine. A warning about a nativized or missing parent is not.</li>
<li>Blueprint nativization from UE4 is gone. Shipping performance comes from moving hot paths to C++, not from a nativize checkbox.</li>
</ul>
</div></div>
<div class="card"><h3>Class design</h3><div class="body">
<ul>
<li>Put shared behavior in a C++ base or a Blueprint function library. Child Blueprints should mostly set data.</li>
<li>Construction Script builds editor-time components and spline points. BeginPlay starts gameplay.</li>
<li>Replicated Blueprints: mark variables replicated, use RepNotify when the client must react, and keep the authority path in one function. Iris (production-ready in 5.8) does not remove the need to decide what replicates.</li>
<li>Components you add in the Blueprint editor are the ones designers expect to move. Adding them only in Construction Script surprises the next person.</li>
</ul>
</div></div>
<div class="card"><h3>Data</h3><div class="body">
<ul>
<li>Expose tunables as variables with categories, tooltips, and clamps in the details metadata.</li>
<li>Data Assets and Data Tables hold rows. Primary Data Assets participate in the Asset Manager.</li>
<li>Enumerations and gameplay tags beat long string compares.</li>
<li>Soft object references on a Blueprint variable do not load the asset until you resolve them.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/BlueprintMath/index.html",
    "Math in Blueprints",
    "Build math the way the graph wants it: small pure functions, expressions, and libraries.",
    """
<h2>Where math should live</h2>
<div class="card"><h3>Three options</h3><div class="body">
<ol>
<li><strong>Math Expression</strong> node. Type <code>sin(deg*pi/180)*radius</code> in one node. Best for a formula you would otherwise spell with ten nodes.</li>
<li><strong>Pure function</strong> on the Blueprint or in a Blueprint Function Library. Best when the same formula is used in several graphs and you want input pins with names.</li>
<li><strong>C++ <code>BlueprintPure</code> function</strong> in a <code>UBlueprintFunctionLibrary</code>. Best when the math is hot, tested, or already exists in <code>FMath</code>.</li>
</ol>
<p>UE5 world coordinates are large. Transform locations use double precision. Blueprint float pins are still single precision unless you are on a double pin (vector components pulled from a transform are handled by the engine nodes). Do not hand-roll a double type with two floats.</p>
</div></div>
<div class="card"><h3>Math Expression examples</h3><div class="body">
<pre>clamp(alpha, 0, 1)
lerp(a, b, alpha)
saturate((value - min) / (max - min))
dot(normalize(direction), forward)
length(target - origin)
atan2(y, x) * 180 / pi</pre>
<p>Names in the expression become input pins. Keep the expression to one idea. If you need branches, use a function with Branch, not a giant expression.</p>
</div></div>
<h2>Recipes</h2>
<div class="card"><h3>Map a range</h3><div class="body">
<p>Use <strong>Map Range Clamped</strong> when a 0–1 input should become a speed, a volume, or a color channel. Unclamped map range will extrapolate past the ends. That is useful for extrapolation and wrong for a health bar.</p>
</div></div>
<div class="card"><h3>Direction and distance</h3><div class="body">
<ol>
<li><strong>Get Unit Direction (Vector)</strong> from A to B, or subtract and <strong>Normalize</strong>.</li>
<li><strong>Distance (Vector)</strong> or <strong>Vector Length</strong> of the difference. Length squared is cheaper when you only compare against a radius squared.</li>
<li><strong>Find Look at Rotation</strong> when an actor should face a point. Combine with <strong>RInterp To</strong> on tick if it should turn smoothly. Pass delta seconds. Do not hard-code 0.016.</li>
<li><strong>Dot product</strong> of two normals tells you facing. 1 is the same direction, 0 is perpendicular, -1 is opposite.</li>
<li><strong>Cross product</strong> gives a perpendicular vector. Use it to build an orthonormal basis, not as a general "rotation" node.</li>
</ol>
</div></div>
<div class="card"><h3>Interpolation</h3><div class="body">
<ul>
<li><strong>Lerp</strong> is a blend by alpha. Alpha 0 returns A, alpha 1 returns B. It does not ease over time by itself.</li>
<li><strong>FInterp To</strong>, <strong>VInterp To</strong>, and <strong>RInterp To</strong> move toward a target using delta time. They are the tick-friendly versions.</li>
<li><strong>Ease</strong> nodes shape a 0–1 alpha before you lerp.</li>
<li>Constant interp speed ignores frame rate. Multiplying a raw speed by delta time is the other correct pattern. Mixing them double-applies time.</li>
</ul>
</div></div>
<div class="card"><h3>Angles</h3><div class="body">
<ul>
<li>Blueprint rotator nodes speak degrees. <code>sin</code> and <code>cos</code> in expressions often speak radians. Convert at the boundary.</li>
<li><strong>Delta (Rotator)</strong> and normalize-axis nodes keep you off 0/360 pops.</li>
<li>Combine rotators only when you know the order. Prefer <strong>Compose Rotators</strong> or a transform multiply over adding pitch, yaw, and roll by hand.</li>
</ul>
</div></div>
<div class="card"><h3>A library function</h3><div class="body">
<p>Create a Blueprint Function Library, add a pure function <code>CritChance</code> with inputs <code>Base</code>, <code>Bonus</code>, <code>ClampMax</code>, and a float return. Body: Map Range or a Math Expression <code>clamp(base+bonus, 0, clampMax)</code>. Call it from any Blueprint. If profiling shows it on the hot path, move that one function to C++:</p>
<pre>UFUNCTION(BlueprintPure, Category="Combat")
static double CritChance(double Base, double Bonus, double ClampMax)
{
    return FMath::Clamp(Base + Bonus, 0.0, ClampMax);
}</pre>
<p>The matching nodes for Min, Max, Lerp, and Clamp are already on the C++ cheat sheet home page.</p>
</div></div>
<div class="card"><h3>Random</h3><div class="body">
<p>Use Random Float in Range and Random Integer in Range. For loot that must repeat in a replay, use a Random Stream variable and seed it. Unseeded random nodes pull from the global stream and will not reproduce a bug.</p>
</div></div>
""",
)

page(
    "Reference/Validation/index.html",
    "Asset validation",
    "Checkers that run against Blueprints and other assets before they reach a cook.",
    """
<h2>What a checker is</h2>
<div class="card"><h3>Data Validation plugin</h3><div class="body">
<p>Enable the Data Validation plugin. The editor then runs validators when you save, when you submit (if your source control is hooked up), and when you run the validation commandlet. This is the supported way to associate a checker with a Blueprint.</p>
<ul>
<li><code>UEditorValidatorBase</code> subclasses live in an editor module. Implement <code>CanValidateAsset</code> and <code>ValidateLoadedAsset</code>.</li>
<li>Return <code>EDataValidationResult::Invalid</code> and add a message with an asset path so the Data Validation window can open the offender.</li>
<li>Actors and components can override <code>IsDataValid</code>. A Blueprint child inherits that C++ check, so the checker follows every designer subclass.</li>
<li>The Asset Audit window lists results across a folder. Use it in reviews, not only on submit.</li>
</ul>
</div></div>
<div class="card"><h3>A Blueprint checker</h3><div class="body">
<pre>bool UBlueprintNamingValidator::CanValidateAsset_Implementation(
    const FAssetData&amp; AssetData, UObject* Asset, FDataValidationContext&amp; Context) const
{
    return Asset &amp;&amp; Asset-&gt;IsA&lt;UBlueprint&gt;();
}

EDataValidationResult UBlueprintNamingValidator::ValidateLoadedAsset_Implementation(
    const FAssetData&amp; AssetData, UObject* Asset, FDataValidationContext&amp; Context)
{
    const UBlueprint* Blueprint = CastChecked&lt;UBlueprint&gt;(Asset);
    const FString Name = Blueprint-&gt;GetName();
    if (!Name.StartsWith(TEXT("BP_")))
    {
        AssetFails(Asset, FText::FromString(TEXT("Blueprint assets must use the BP_ prefix.")), Context);
        return EDataValidationResult::Invalid;
    }
    AssetPasses(Asset);
    return EDataValidationResult::Valid;
}</pre>
<p>More useful checks than prefixes:</p>
<ul>
<li>The generated class has a required component or interface.</li>
<li>Soft paths are set, hard references to the giant master material are not.</li>
<li>Tick is disabled on actors that were marked as decorative.</li>
<li>Nanite is enabled on static meshes in <code>/Game/Environment</code> and disabled on translucent VFX meshes.</li>
<li>A primary asset has a cook bundle and a valid Asset Manager label.</li>
</ul>
</div></div>
<div class="card"><h3>IsDataValid on the actor</h3><div class="body">
<pre>#if WITH_EDITOR
EDataValidationResult APickup::IsDataValid(FDataValidationContext&amp; Context) const
{
    EDataValidationResult Result = Super::IsDataValid(Context);
    if (Amount &lt;= 0)
    {
        Context.AddError(FText::FromString(TEXT("Pickup Amount must be positive.")));
        Result = EDataValidationResult::Invalid;
    }
    return Result;
}
#endif</pre>
<p>This runs for the C++ class and for Blueprint children. Put gameplay rules here. Put asset-wide policy (naming, folders, Nanite) in an editor validator so it can see meshes and materials that are not actors.</p>
</div></div>
<div class="card"><h3>Run it</h3><div class="body">
<ul>
<li>Editor: Tools or the Content Browser context menu for Validate Assets, depending on version. The Data Validation tab collects messages.</li>
<li>Commandlet: cook and CI should call the data validation commandlet on the changelist so a bad Blueprint never reaches the build farm only.</li>
<li>Validators are editor-only. They do not ship in the game module. Keep them out of runtime dependencies.</li>
</ul>
<div class="callout">A checker that loads every referenced world on save will make the editor unusable. Validate the asset you were given. Queue world checks for CI.</div>
</div></div>
""",
)

page(
    "Reference/AssetPipeline/index.html",
    "Asset pipeline",
    "From source file to cooked package, including Interchange, the Asset Manager, and platform textures.",
    """
<h2>Import</h2>
<div class="card"><h3>Interchange</h3><div class="body">
<p>Interchange is the UE5 import framework for FBX, glTF, USD, and MaterialX. It replaces the older one-off FBX paths as the default in current engines. 5.8 fixes include MaterialX primvar baking cases; if a look breaks on reimport, check the Interchange stack before you hand-edit the material.</p>
<ul>
<li>Reimport preserves engine-side settings when the source path is intact. Breaking the source path and reimporting as a new asset loses Nanite flags, collision, and LOD settings.</li>
<li>Nanite enable, distance field, and collision complexity are mesh properties. Set them in the static mesh editor or a validator, not in the DCC file name.</li>
<li>USD and MaterialX matter for teams round-tripping with film tools. Game teams can stay on FBX or glTF if that is the whole pipe.</li>
</ul>
</div></div>
<h2>Cook and chunks</h2>
<div class="card"><h3>Asset Manager</h3><div class="body">
<ul>
<li>Primary Asset types (maps, items, abilities) are labels the Asset Manager scans.</li>
<li>Cook rules decide what is always cooked, cooked in a chunk, or left out. An unreferenced Blueprint is not in the package unless a manager, a redirector, or an always-cook path names it.</li>
<li>Chunks map to install packs. Put the first level in chunk 0 and optional biomes in later chunks.</li>
<li>Soft references are how you point at an asset without cooking a hard edge from your player Blueprint into every skin.</li>
</ul>
</div></div>
<div class="card"><h3>Redirectors and folders</h3><div class="body">
<p>Moving an asset leaves a redirector so old references resolve. Fix up redirectors before you cook a release. A chain of redirectors is a load-time tax and a source of "missing" assets that are only mis-pathed.</p>
<p>Use folders as ownership boundaries (Characters, Environment, UI, Audio). Validators can then apply Nanite or texture rules per folder.</p>
</div></div>
<div class="card"><h3>Textures and meshes per platform</h3><div class="body">
<table>
<tr><th>Platform</th><th>Typical texture format</th></tr>
<tr><td>Windows, Xbox, PlayStation</td><td>BC / DXT family (BC7 for color, BC5 for normals)</td></tr>
<tr><td>Android and iOS</td><td>ASTC. ETC2 is the Android fallback where ASTC is missing</td></tr>
</table>
<ul>
<li>Set maximum LOD size per texture group in the device profile memory buckets. A phone profile should not stream the cinematic 4K group.</li>
<li>Virtual textures help unique large terrain. They are not a win for small UI icons.</li>
<li>Nanite data cooks into the mesh. Platforms that cannot render it still need the fallback mesh in the cook.</li>
</ul>
</div></div>
<div class="card"><h3>Derived Data Cache</h3><div class="body">
<p>Shaders and Nanite builds land in the Derived Data Cache. A shared DDC (including Zen storage in current engines) keeps the team from rebuilding the same mesh. If only one machine shows a Nanite artifact, compare DDC and engine hotfix before you blame the source art.</p>
</div></div>
""",
)

page(
    "Reference/Deployment/index.html",
    "Deployment",
    "Cook, package, and get a Development build onto a device you can profile.",
    """
<h2>Build types</h2>
<div class="card"><h3>Which configuration</h3><div class="body">
<table>
<tr><th>Configuration</th><th>Use</th></tr>
<tr><td>Debug</td><td>Breakpoints in engine code. Too slow to judge frame time.</td></tr>
<tr><td>Development</td><td>Device profiling, Insights, stat commands, logs.</td></tr>
<tr><td>Test</td><td>Closer to shipping, fewer debugging tools.</td></tr>
<tr><td>Shipping</td><td>What players run. No stat overlay unless you left a backdoor.</td></tr>
</table>
<p>Profile Development on the metal you will ship, then confirm Shipping separately because logging and checks change the numbers.</p>
</div></div>
<div class="card"><h3>Cook and stage</h3><div class="body">
<ol>
<li>Set maps to cook, cultures, and the default map in Project Settings → Packaging.</li>
<li>Platforms menu: choose the target, then Package Project, or use Project Launcher / Turnkey for repeatable profiles.</li>
<li>Cook on the farm or locally. Iterative cooks are for day-to-day device hops. A clean cook is for release candidates.</li>
<li>5.8 Android cooks skip more unchanged assets. Still do a clean cook before you declare a memory win.</li>
<li>Install the staged build with the platform tool (Explorer, adb, Xcode/ios-deploy, or the console deployment tool from the partner SDK).</li>
</ol>
<pre>RunUAT.bat BuildCookRun -project=Your.uproject -platform=Win64 -clientconfig=Development -build -cook -stage -pak -archive</pre>
<p class="note">Swap <code>-platform=Android</code> or <code>IOS</code> when the SDK is installed. Console platform names appear only after that platform's extension is installed.</p>
</div></div>
<div class="card"><h3>Launch a profiled session</h3><div class="body">
<pre>-trace=cpu,gpu,frame,bookmark,counters -statnamedevents -tracehost=YOUR_PC_IP
-ExecCmds="r.GPUStatsEnabled 1,stat unit"</pre>
<p>On Android, <code>adb logcat</code> shows the log. On iOS, use the Mac console or the device log. On consoles, use the partner target manager plus Insights pointed at the kit.</p>
<p>The Unreal Engine Remote app in 5.8 is for mobile input from the editor. It does not replace a packaged profile capture.</p>
</div></div>
<div class="card"><h3>Settings to lock before a platform build</h3><div class="body">
<ul>
<li>Scalability default and device profile cvars, not editor previews.</li>
<li>Texture groups and pool sizes for that memory bucket.</li>
<li>Lighting method the device can run (see each platform page).</li>
<li>PSO precaching enabled so the first session is not a shader-compile demo.</li>
<li>Logging verbosity down in Shipping.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Platforms/Windows/index.html",
    "Windows",
    "Desktop settings for Nanite, Lumen, and a scalable PC.",
    """
<h2>Renderer</h2>
<div class="card"><h3>Defaults that match the features</h3><div class="body">
<ul>
<li>DirectX 12 and Shader Model 6 for Nanite, virtual shadow maps, hardware ray tracing, and reliable Lumen.</li>
<li>DirectX 11 is a compatibility target. Treat it as a reduced path: no Nanite, and do not depend on Lumen after the 5.5 SM5 issues.</li>
<li>Vulkan on Windows is a useful comparison RHI, not the default shipping choice for most games.</li>
</ul>
<pre>[/Script/WindowsTargetPlatform.WindowsTargetSettings]
DefaultGraphicsRHI=DefaultGraphicsRHI_DX12

; DefaultEngine.ini, kept honest in source control
r.Nanite=1
r.DynamicGlobalIlluminationMethod=1
r.ReflectionMethod=1</pre>
<p class="note">Prefer the Project Settings UI so the ini keys match your hotfix. Copying stale keys from a 5.1 tutorial is a common way to silently disable a feature.</p>
</div></div>
<div class="card"><h3>Scalability</h3><div class="body">
<p>Ship a scalability ladder instead of one cinematic setting.</p>
<ul>
<li>Epic / Cinematic: Nanite, Lumen High, VSM, MegaLights, TSR at a moderate screen percentage.</li>
<li>High: the 60 fps target. Drop reflection quality and shadow quality before you disable GI.</li>
<li>Medium / Low: Lumen Lite on 5.8, or screen-space GI plus baked sky, lower resolution scale, fewer shadow pages.</li>
<li>Store overrides in <code>Config/DefaultScalability.ini</code> and let players change them with the scalability API or a settings Blueprint.</li>
</ul>
</div></div>
<div class="card"><h3>Profile</h3><div class="body">
<ul>
<li>Unreal Insights locally, <code>ProfileGPU</code>, and PIX for a single D3D12 frame.</li>
<li>Test minimum-spec GPUs, not only the machine that builds lighting.</li>
<li>Windowed mode and VSync hide frame time. Use <code>r.VSync 0</code> and an unlocked frame rate while measuring, then decide the shipping cap.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Platforms/Android/index.html",
    "Android",
    "Device profiles, Vulkan, and where Lumen is allowed to exist.",
    """
<h2>Renderer choice</h2>
<div class="card"><h3>Mobile renderer first</h3><div class="body">
<p>Most phones should use the mobile renderer and one of Epic's lighting tiers: LDR, basic static lighting, full HDR static, or HDR plus a single per-pixel directional light. That is the path that reaches mid and low devices.</p>
<p>The desktop renderer (Vulkan, Shader Model 5) is an opt-in for high-end devices. Experimental Lumen on Android, documented for 5.4 and still the documented mobile path in 5.7, hangs off that renderer. iOS does not get the same path.</p>
</div></div>
<div class="card"><h3>Project settings to set on purpose</h3><div class="body">
<ul>
<li>Package name, minimum and target SDK, orientation, and graphics API list: Vulkan preferred, GLES only if you still need older devices.</li>
<li><code>r.Android.DisableVulkanSupport=0</code> when you want Vulkan.</li>
<li><code>r.Android.DisableVulkanSM5Support=0</code> only when you are opting high devices into the desktop renderer.</li>
<li>Mobile HDR on for any lit tier. Off only for the LDR unlit tier.</li>
<li>ASTC as the texture format. Keep ETC2 as fallback if your device list needs it.</li>
<li>Forward shading or the mobile deferred path as your art direction requires. Deferred costs more and is not required for the static-light tiers.</li>
<li>5.8: use the automated SDK setup, then still confirm licenses and NDK paths on the build machine.</li>
</ul>
</div></div>
<h2>Device profiles</h2>
<div class="card"><h3>DefaultDeviceProfiles.ini</h3><div class="body">
<p>Window → Developer Tools → Device Profiles, and check the result into <code>Config/DefaultDeviceProfiles.ini</code>. Profiles inherit. Android's selector matches GPU families onto buckets such as Low, Mid, and High, plus Vulkan SM5 profiles when you extend them.</p>
<pre>[Android_Low DeviceProfile]
BaseProfileName=Android
+CVars=r.MobileContentScaleFactor=0.7
+CVars=r.MaterialQualityLevel=0
+CVars=sg.ShadowQuality=0
+CVars=sg.EffectsQuality=0

[Android_High DeviceProfile]
BaseProfileName=Android
+CVars=r.MobileContentScaleFactor=1.0
+CVars=sg.ShadowQuality=2

[Android_High_Lumen DeviceProfile]
BaseProfileName=Android_Vulkan_SM5
; Only devices you have captured at frame time belong here.
+CVars=r.DynamicGlobalIlluminationMethod=1</pre>
<p>Match rules belong in the profile selector so an unknown GPU falls down to Low, never up to Lumen.</p>
<ul>
<li>Memory buckets cap texture LOD group sizes. Set them in the Android engine config and reference the bucket from the profile.</li>
<li>Preview in the editor with the Android previewer and Shader Complexity before you package.</li>
<li>5.8 Platform Preview and the Remote app help input and look. Frame time still comes from a packaged Development build.</li>
</ul>
</div></div>
<div class="card"><h3>Profile on device</h3><div class="body">
<pre>adb install -r YourGame.apk
adb logcat -s UE
adb shell am start -n com.your.game/com.epicgames.unreal.GameActivity --es trace cpu,gpu,frame</pre>
<p>Pull <code>.utrace</code> files from the game's saved directory if you used <code>-tracefile</code>. GPU counters from the vendor (Adreno, Mali) explain fill-rate problems Insights only labels as the mobile base pass.</p>
</div></div>
""",
)

page(
    "Reference/Platforms/iOS/index.html",
    "iOS",
    "Metal, content scale, and a lighting setup that does not depend on Lumen.",
    """
<h2>What the platform can run</h2>
<div class="card"><h3>Constraints</h3><div class="body">
<ul>
<li>Metal only. There is no Vulkan and no DirectX fallback on device.</li>
<li>Lumen is not supported on iOS, iPadOS, or tvOS in Epic's mobile Lumen documentation. Do not light a level only with Lumen and expect the iOS cook to invent lightmaps.</li>
<li>Nanite is a desktop feature. Ship classic LODs or a Nanite fallback mesh that you have actually viewed in the mobile previewer.</li>
<li>You need a Mac with Xcode to sign and deploy, even if the editor is on Windows (remote build).</li>
</ul>
</div></div>
<div class="card"><h3>Settings</h3><div class="body">
<ul>
<li>Bundle id, signing team, minimum iOS version, and device orientations in the iOS project settings.</li>
<li>Metal shader version and the mobile renderer aligned with your lighting tier.</li>
<li>Mobile HDR on for lit games. One stationary directional light for the sun if you need per-pixel lighting. Everything else static.</li>
<li>Reflection captures instead of Lumen reflections.</li>
<li>ASTC textures. Smaller max LOD sizes on older phones via device profiles.</li>
<li><code>r.MobileContentScaleFactor</code> per device in <code>DefaultDeviceProfiles.ini</code>. A full-resolution modern phone and an older phone should not share a scale.</li>
<li>Disable features you cannot pay for: virtual shadow maps, hardware ray tracing, high translucency, and heavy post (bloom off on the low tier).</li>
</ul>
<pre>[iPhone_Low DeviceProfile]
BaseProfileName=IOS
+CVars=r.MobileContentScaleFactor=0.75
+CVars=r.BloomQuality=0
+CVars=sg.PostProcessQuality=0

[iPhone_High DeviceProfile]
BaseProfileName=IOS
+CVars=r.MobileContentScaleFactor=1.0
+CVars=sg.ShadowQuality=2</pre>
<p>iOS profile names follow the device. Extend <code>BaseDeviceProfiles</code> rather than replacing the whole family, and add new phones (the 5.5 notes called out missing devices such as iPhone 16e) when the selector does not know them.</p>
</div></div>
<div class="card"><h3>Deploy and profile</h3><div class="body">
<ol>
<li>Package for iOS from a machine that can see the Mac build service.</li>
<li>Install a Development build through Xcode so you keep logs and Insights.</li>
<li>Capture on device. The editor's mobile previewer is a shader and layout check, not a thermal check.</li>
<li>Watch thermals over several minutes. A one-second <code>stat unit</code> will not show the GPU clock drop.</li>
</ol>
</div></div>
""",
)

page(
    "Reference/Platforms/PlayStation/index.html",
    "PlayStation",
    "Unreal-side setup you can keep in this repo. Partner-portal budgets stay in the Sony program.",
    """
<h2>Access</h2>
<div class="card"><h3>What this page will and will not claim</h3><div class="body">
<p>PlayStation development uses a platform extension and SDK that Epic and Sony provide after you are in the PlayStation Partners program. Those docs include certification requirements and kit-specific tools. They are not copied here.</p>
<div class="ok">Once the extension is installed, the editor gains a PlayStation platform, a config directory for that platform, device profiles, and a package target. The settings below are the Unreal project choices you still make yourself.</div>
</div></div>
<h2>Project choices</h2>
<div class="card"><h3>Current generation</h3><div class="body">
<ul>
<li>Treat PlayStation 5 as a Nanite, Lumen, virtual shadow map, and MegaLights target. MegaLights is production-ready in 5.8 with 60 fps console play in mind.</li>
<li>Resolution scale and TSR do as much for the frame as any single cvar. Set them in the platform scalability or device profile, not only in the editor viewport.</li>
<li>Use Lumen High for a 30 fps quality mode and a tighter GI scalability, or Lumen Lite where 5.8 and your art direction allow a 60 fps mode.</li>
<li>Cook a Development build to the kit for Insights. Shipping comes after memory and certification passes.</li>
<li>PSO precache matters on consoles the same way it matters on PC. A hitch that only happens on the first encounter is often shaders.</li>
</ul>
</div></div>
<div class="card"><h3>Config layout</h3><div class="body">
<ul>
<li><code>Config/&lt;Platform&gt;/&lt;Platform&gt;Engine.ini</code> for cvars that must not apply to Windows.</li>
<li><code>Config/DefaultDeviceProfiles.ini</code> entries whose base profile is the console, if you ship more than one performance mode (quality and performance).</li>
<li>Separate texture and memory settings from the mobile buckets so a phone profile never becomes the parent of a console profile.</li>
<li>Platform-specific Blueprint nodes belong behind a platform macro or a subsystem, so the Windows editor build still loads.</li>
</ul>
<pre>; Illustrative only. Use the ini names the installed platform extension writes.
[PS5_Performance DeviceProfile]
+CVars=sg.ResolutionQuality=70
+CVars=sg.GlobalIlluminationQuality=2
+CVars=sg.ShadowQuality=2

[PS5_Quality DeviceProfile]
+CVars=sg.ResolutionQuality=85
+CVars=sg.GlobalIlluminationQuality=3</pre>
</div></div>
<div class="card"><h3>Profile</h3><div class="body">
<ul>
<li>Unreal Insights with the GPU channel, over the kit connection described in the platform extension.</li>
<li>The platform GPU capture tool from the SDK for a single frame the Insights name does not explain.</li>
<li><code>stat unit</code> on a Development build in the rooms you actually ship, including the densest Nanite street and the busiest MegaLights interior.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Platforms/Xbox/index.html",
    "Xbox",
    "Unreal-side setup you can keep in this repo. Partner-portal budgets stay in the Microsoft program.",
    """
<h2>Access</h2>
<div class="card"><h3>What this page will and will not claim</h3><div class="body">
<p>Xbox development uses a platform extension and the Microsoft GDK, available through the Xbox program. Certification rules and many kit tools are under that agreement. This page covers the Unreal project layout that sits on top of an installed extension.</p>
<div class="ok">After the extension is installed you get an Xbox platform target, platform config, packaging through the Xbox tools, and PIX on the dev kit for GPU captures.</div>
</div></div>
<h2>Project choices</h2>
<div class="card"><h3>Series consoles</h3><div class="body">
<ul>
<li>Xbox Series X and Series S are the Nanite and Lumen generation. Series S has less GPU and memory. Give it its own device profile instead of hoping the Series X profile scales itself.</li>
<li>DirectX 12 class features (Nanite, VSM, hardware ray tracing where you enable it, MegaLights in 5.8) match this tier.</li>
<li>Set resolution scale per profile. A common split is a higher scale on Series X and a lower scale plus slightly lower GI quality on Series S.</li>
<li>Last-generation Xbox One hardware does not share that feature set. If you still ship it, use a reduced renderer and baked lighting, in its own profile, and do not point it at Nanite-only meshes without fallbacks.</li>
</ul>
</div></div>
<div class="card"><h3>Config layout</h3><div class="body">
<pre>; Illustrative. Match the profile names the GDK platform plugin creates.
[XSX_Quality DeviceProfile]
+CVars=sg.ResolutionQuality=85
+CVars=sg.GlobalIlluminationQuality=3
+CVars=sg.ShadowQuality=3

[XSS_Performance DeviceProfile]
+CVars=sg.ResolutionQuality=65
+CVars=sg.GlobalIlluminationQuality=2
+CVars=sg.ShadowQuality=2
+CVars=r.Streaming.PoolSize=1500</pre>
<ul>
<li>Keep pool sizes in the profile so Series S does not inherit a desktop 4 GB texture pool or a phone pool.</li>
<li>Put achievements, commerce, and sign-in behind the platform's online subsystem, not inside gameplay Blueprints that also run on Windows.</li>
<li>Cook Development for Insights and PIX. Run a Shipping cook before you judge memory, because editor data and debug packages lie.</li>
</ul>
</div></div>
<div class="card"><h3>Profile</h3><div class="body">
<ul>
<li>PIX for a GPU frame on the kit.</li>
<li>Unreal Insights for a session that includes a fast travel and a combat encounter.</li>
<li>Compare Series X and Series S traces side by side before you change a shared material.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/WorldBuilding/index.html",
    "World building",
    "World Partition, PCG, and the 5.8 terrain and vegetation tools.",
    """
<h2>Streaming worlds</h2>
<div class="card"><h3>World Partition</h3><div class="body">
<ul>
<li>One persistent world, actors stored per cell (One File Per Actor). Designers stop locking a single umap for the whole country.</li>
<li>Data Layers toggle sets of actors (story state, lighting scenario) without a second copy of the land.</li>
<li>HLODs stand in for a cell that is loaded but far. Build them. An empty HLOD setup streams full detail too early.</li>
<li>Level Instances and Packed Level Actors reuse a building or a room. They are the replacement for UE4 sublevel copy-paste.</li>
<li>Always loaded is for the player start and the tiny persistent set. Everything else has a loading range.</li>
</ul>
</div></div>
<div class="card"><h3>PCG and vegetation</h3><div class="body">
<ul>
<li>Procedural Content Generation graphs scatter points, filter by slope and layer, and spawn assemblies. 5.8 adds stronger nondestructive edits and graph workflow.</li>
<li>The Procedural Vegetation Editor in 5.8 builds Nanite-ready plants with wind inside the editor.</li>
<li>Runtime generation has a frame cost. Bake to instances or Nanite assemblies when the scatter does not need to change.</li>
<li>Validators should check that PCG output meshes in the environment folder have Nanite and a sane cull distance.</li>
</ul>
</div></div>
<div class="card"><h3>Landscape and Mesh Terrain</h3><div class="body">
<p>Heightfield Landscape remains the tool for rolling terrain. Mesh Terrain in 5.8 is experimental and exists so cliffs, caves, and overhangs are not fighting a heightfield. Do not convert a shipped landscape on a whim. Virtual heightfield and Nanite tessellation settings still apply to the classic landscape path in versions that enable them.</p>
</div></div>
""",
)

page(
    "Reference/Animation/index.html",
    "Animation",
    "Graphs a gameplay programmer touches, and what 5.8 adds in the editor.",
    """
<h2>Runtime</h2>
<div class="card"><h3>Pieces</h3><div class="body">
<ul>
<li><strong>Skeleton, Skeletal Mesh, Animation Blueprint, Anim Sequence, Montage.</strong> The Anim Blueprint runs on the mesh component. Do not also drive the same bones from Tick unless you mean to.</li>
<li><strong>State machines</strong> for locomotion. Blend spaces for speed and direction. Montages for attacks and hits, with slots so they override the upper body only.</li>
<li><strong>Control Rig</strong> for procedural correction and for authoring. 5.8 adds a faster dynamics solver and direct mesh controls so animators touch the mesh instead of a cloud of nulls.</li>
<li><strong>IK Rig and IK Retargeter</strong> move animation between skeletons. Retarget in the pipeline, not with a per-frame Blueprint solver, when the motion is authored.</li>
<li><strong>Chooser and motion matching</strong> pick clips from data instead of a giant state machine. Use them when you have the animation set to feed them.</li>
<li><strong>Linked anim layers</strong> keep a weapon graph separate from locomotion.</li>
</ul>
</div></div>
<div class="card"><h3>What programmers should expose</h3><div class="body">
<ul>
<li>A small set of variables (speed, gait, aim yaw, is-in-air). The graph reads them. Gameplay sets them once per frame or from events, not from ten scattered Blueprints.</li>
<li>Montage play from an ability or a replicated event, with a clear multicast policy.</li>
<li>Animation budgets and update-rate optimization on crowds. MetaHuman crowds in 5.8 are a content system on top of instancing, not a reason to spawn a thousand full Actors.</li>
</ul>
</div></div>
<div class="card"><h3>Sequencer and capture</h3><div class="body">
<ul>
<li>Sequencer for cinematics and for gameplay sequences that are timelines rather than logic.</li>
<li>Movie Render Graph is production-ready in 5.8 for offline renders.</li>
<li>Live Link Hub is production-ready in 5.8 for device hub, sync, and recording.</li>
<li>MetaHuman Animator can take markerless single-camera capture in 5.8. It is an authoring path. The runtime character is still a skeletal mesh with a rig.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Gameplay/index.html",
    "Gameplay systems",
    "The frameworks a new programmer should pick up before inventing their own.",
    """
<h2>Input and ability</h2>
<div class="card"><h3>Enhanced Input</h3><div class="body">
<p>UE5's input system is Enhanced Input. An Input Action is a verb (Jump, Fire). An Input Mapping Context binds keys and gamepad events to actions and can be added per pawn or per mode.</p>
<ul>
<li>Triggers and modifiers (hold, tap, dead zone, sway) live on the mapping, not in a chain of Blueprint branches on Tick.</li>
<li>Add and remove mapping contexts when you pause or enter a vehicle. Do not leave the UI context active under the game.</li>
</ul>
</div></div>
<div class="card"><h3>Gameplay Ability System</h3><div class="body">
<p>GAS is a plugin. Abilities, attributes, gameplay effects, and tags cover combat rules you would otherwise rewrite in Blueprints. Use it when you have cooldowns, prediction, and stacking buffs. A single-player walking sim does not need it.</p>
<p>Tags (<code>FGameplayTag</code>) are the shared language between abilities, animation choosers, and UI. Define them in the project tag table, not as raw strings.</p>
</div></div>
<h2>AI and flow</h2>
<div class="card"><h3>Behavior trees, State Trees, EQS</h3><div class="body">
<ul>
<li>Behavior trees remain the classic AI graph. Tasks should be short. Latent tasks must end.</li>
<li>State Trees are the newer state machine for AI and for gameplay objects. Prefer them for new work in 5.5+ if your team has learned them.</li>
<li>EQS picks a location. It is not an AI brain. Cache queries; do not run a dense test every tick.</li>
<li>Smart Objects advertise interactable spots to AI.</li>
<li>Mass Entity is the crowd/ECS framework when Actors are too heavy. MetaHuman crowd content in 5.8 is aimed at that scale.</li>
</ul>
</div></div>
<div class="card"><h3>Other systems worth knowing</h3><div class="body">
<ul>
<li><strong>Game Features and plugins</strong> load a slice of content (a mode, a season) without cooking it into the base pawn.</li>
<li><strong>Common UI</strong> for layered menus, gamepad focus, and activation stacks.</li>
<li><strong>Data Registries</strong> and the Asset Manager for item databases.</li>
<li><strong>Gameplay Targeting and cameras</strong> (gameplay camera system) when camera code has outgrown a spring arm.</li>
<li><strong>Modeling Mode and Geometry Script</strong> for tools and runtime mesh edits. Geometry Script is Blueprint-accessible mesh math; keep heavy booleans off the game thread.</li>
</ul>
</div></div>
""",
)

page(
    "Reference/Audio/index.html",
    "Audio and Niagara",
    "MetaSounds, Niagara, and the Insights view that landed as production-ready in 5.8.",
    """
<h2>Audio</h2>
<div class="card"><h3>MetaSounds</h3><div class="body">
<p>MetaSounds is the UE5 audio graph. Sources are MetaSound assets, not only Sound Cues. You build generators, filters, and triggers in a graph that can take parameters from gameplay (RPM, wind, surface type).</p>
<ul>
<li>Concurrency and attenuation live on the sound so a hundred footfalls do not all play at full volume and full voice count.</li>
<li>Quartz is the sample-accurate clock when music and gameplay must line up.</li>
<li>Audio Insights is production-ready in 5.8. Capture it when you suspect a hitch is a wave decode or a voice spike rather than Nanite.</li>
<li>Compression and streaming settings belong in the platform profile. A cinematic wav should not be the phone default.</li>
</ul>
</div></div>
<h2>VFX</h2>
<div class="card"><h3>Niagara</h3><div class="body">
<ul>
<li>Niagara systems and emitters replace Cascade. Use GPU sim for large counts and CPU sim when gameplay must read positions.</li>
<li>Scalability on the emitter (spawn rate per quality) belongs in the effect, then follows <code>sg.EffectsQuality</code>.</li>
<li>Overdraw kills mobile and also shows up in front of Lumen reflections. Shader Complexity and Quad Overdraw are the views.</li>
<li>A Niagara system hard-referenced by a character loads with that character. Soft-reference rare ultimates.</li>
</ul>
</div></div>
<div class="card"><h3>Chaos cloth and destruction</h3><div class="body">
<p>5.8 makes Dataflow production-ready for cloth and destruction authoring, and adds the Chaos Cloth Panel Editor. Simulate at the rate the camera can see. Authoring-time simulation does not have to be the runtime budget.</p>
</div></div>
""",
)

page(
    "Reference/Networking/index.html",
    "Networking",
    "Replication basics and Iris, which is production-ready in 5.8.",
    """
<h2>Classic replication</h2>
<div class="card"><h3>Rules that still hold</h3><div class="body">
<ul>
<li>The server owns gameplay. Clients predict movement and cosmetics when you deliberately set that up.</li>
<li><code>bReplicates</code> on the actor, replicated properties, and RPCs (<code>Server</code>, <code>Client</code>, <code>NetMulticast</code>) are the Blueprint surface.</li>
<li>Relevancy and dormancy decide who gets updates. A tight relevancy radius beats a smaller vector.</li>
<li>Reliable RPCs that fire every shot will blow the reliable buffer. Batch, or use a replicated variable.</li>
<li>Listen servers and dedicated servers both use the same replication. Package a server target when you need a headless process.</li>
<li>Online subsystem (EOS or another) handles sessions and identity. It is not the replication system.</li>
</ul>
</div></div>
<div class="card"><h3>Iris</h3><div class="body">
<p>Iris is the newer replication system. 5.8 marks it production-ready. It changes how properties are described and pushed so large actor counts cost less. Adoption is a project decision: read the Iris setup for your hotfix, enable it on a branch, and compare a network Insights capture against the classic driver before you flip the default.</p>
<p>Design habits do not change. You still decide authority, prediction, and what is cosmetic.</p>
</div></div>
<div class="card"><h3>Profile</h3><div class="body">
<ul>
<li><code>stat net</code> for a coarse view.</li>
<li>Network insights in a trace when you need per-actor cost.</li>
<li>Test with packet lag and loss emulation, not only on localhost. Localhost hides ordering bugs.</li>
</ul>
</div></div>
""",
)

print("done", len(NAV))
