<h2>album object (full)</h2>
<table id="tablepress-51" class="tablepress table tablepress-id-51">
<thead>
<tr class="row-1 odd">
	<th class="column-1">Key<br>
</th><th class="column-2">Value&nbsp;Type <br>
</th><th class="column-3">Value Description<br>
</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">album_type <br>
</td><td class="column-2">string <br>
</td><td class="column-3">The type of the album: one of <code>"album"</code>, <code>"single"</code>, or <code>"compilation"</code>. <br>
</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">artists <br>
</td><td class="column-2">array of simplified <a href="/web-api/object-model/#artist-object-simplified">artist objects</a> <br>
</td><td class="column-3">The artists of the album. Each artist object includes a link in <code>href</code> to more detailed information about the artist.<br>
</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">available_markets <br>
</td><td class="column-2">array of strings <br>
</td><td class="column-3">The markets in which the album is available: <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2 country codes</a>. Note that an album is considered available in a market when at least 1 of its tracks is available in that market.<br>
</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">copyrights</td><td class="column-2">array of <a href="/web-api/object-model/#copyright-object">copyright objects</a><br>
</td><td class="column-3">The copyright statements of the album.</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">external_ids <br>
</td><td class="column-2">an <a href="/web-api/object-model/#external-id-object">external ID object</a><br>
</td><td class="column-3">Known external IDs for the album. <br>
</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">external_urls</td><td class="column-2">an <a href="/web-api/object-model/#external-url-object">external URL object</a></td><td class="column-3">Known external URLs for this album.</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">genres </td><td class="column-2">array of strings <br>
</td><td class="column-3">A list of the genres used to classify the album. For example: <code>"Prog Rock"</code>, <code>"Post-Grunge"</code>. (If not yet classified, the array is empty.) <br>
</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">href</td><td class="column-2">string</td><td class="column-3">A link to the Web API endpoint providing full details of the album.</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">id <br>
</td><td class="column-2">string <br>
</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify ID</a> for the album. <br>
</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">images <br>
</td><td class="column-2">array of <a href="/web-api/object-model/#image-object">image objects</a><br>
</td><td class="column-3">The cover art for the album in various sizes, widest first.</td>
</tr>
<tr class="row-12 even">
	<td class="column-1">label</td><td class="column-2">string</td><td class="column-3">The label for the album.</td>
</tr>
<tr class="row-13 odd">
	<td class="column-1">name <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The name of the album.  In case of an album takedown, the value may be an empty string.</td>
</tr>
<tr class="row-14 even">
	<td class="column-1">popularity <br>
</td><td class="column-2">integer</td><td class="column-3">The popularity of the album. The value will be between 0 and 100, with 100 being the most popular. The popularity is calculated from the popularity of the album's individual tracks.</td>
</tr>
<tr class="row-15 odd">
	<td class="column-1">release_date <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The date the album was first released, for example <code>"1981-12-15"</code>. Depending on the precision, it might be shown as <code>"1981"</code> or <code>"1981-12"</code>.<br>
</td>
</tr>
<tr class="row-16 even">
	<td class="column-1">release_date_<br>
precision</td><td class="column-2">string</td><td class="column-3">The precision with which <code>release_date</code> value is known: <code>"year"</code>, <code>"month"</code>, or <code>"day"</code>.</td>
</tr>
<tr class="row-17 odd">
	<td class="column-1">tracks <br>
</td><td class="column-2">array of simplified <a href="/web-api/object-model/#track-object-simplified">track objects</a> inside a <a href="/web-api/object-model/#paging-object">paging object</a> </td><td class="column-3">The tracks of the album.<br>
</td>
</tr>
<tr class="row-18 even">
	<td class="column-1">type <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The object type: "album"<br>
</td>
</tr>
<tr class="row-19 odd">
	<td class="column-1">uri</td><td class="column-2">string</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify URI</a> for the album.</td>
</tr>
</tbody>
</table>

<h2>artist object (full)</h2><table id="tablepress-52" class="tablepress table tablepress-id-52">
<thead>
<tr class="row-1 odd">
	<th class="column-1">Key <br>
</th><th class="column-2">Value&nbsp;Type <br>
</th><th class="column-3">Value Description <br>
</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">external_urls</td><td class="column-2">an <a href="/web-api/object-model/#external-url-object">external URL object</a></td><td class="column-3">Known external URLs for this artist.</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">followers</td><td class="column-2">A <a href="/web-api/object-model/#followers-object"> followers object</a></td><td class="column-3">Information about the followers of the artist. </td>
</tr>
<tr class="row-4 even">
	<td class="column-1">genres <br>
</td><td class="column-2">array of strings<br>
</td><td class="column-3">A list of the genres the artist is associated with. For example: <code>"Prog Rock"</code>, <code>"Post-Grunge"</code>. (If not yet classified, the array is empty.) <br>
</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">href</td><td class="column-2">string</td><td class="column-3">A link to the Web API endpoint providing full details of the artist.</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">id <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The<a href="/web-api/user-guide/#spotify-uris-and-ids"> Spotify ID</a> for the artist. <br>
</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">images <br>
</td><td class="column-2">array of <a href="/web-api/object-model/#image-object">image objects</a><br>
</td><td class="column-3">Images of the artist in various sizes, widest first.</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">name <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The name of the artist </td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">popularity <br>
</td><td class="column-2">int<br>
</td><td class="column-3">The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.<br>
</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">type <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The object type: <code>"artist"</code><br>
</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">uri</td><td class="column-2">string</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify URI</a> for the artist.</td>
</tr>
</tbody>
</table>
<table id="tablepress-52" class="tablepress table tablepress-id-52">
<thead>
<tr class="row-1 odd">
	<th class="column-1">Key <br>
</th><th class="column-2">Value&nbsp;Type <br>
</th><th class="column-3">Value Description <br>
</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">external_urls</td><td class="column-2">an <a href="/web-api/object-model/#external-url-object">external URL object</a></td><td class="column-3">Known external URLs for this artist.</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">followers</td><td class="column-2">A <a href="/web-api/object-model/#followers-object"> followers object</a></td><td class="column-3">Information about the followers of the artist. </td>
</tr>
<tr class="row-4 even">
	<td class="column-1">genres <br>
</td><td class="column-2">array of strings<br>
</td><td class="column-3">A list of the genres the artist is associated with. For example: <code>"Prog Rock"</code>, <code>"Post-Grunge"</code>. (If not yet classified, the array is empty.) <br>
</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">href</td><td class="column-2">string</td><td class="column-3">A link to the Web API endpoint providing full details of the artist.</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">id <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The<a href="/web-api/user-guide/#spotify-uris-and-ids"> Spotify ID</a> for the artist. <br>
</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">images <br>
</td><td class="column-2">array of <a href="/web-api/object-model/#image-object">image objects</a><br>
</td><td class="column-3">Images of the artist in various sizes, widest first.</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">name <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The name of the artist </td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">popularity <br>
</td><td class="column-2">int<br>
</td><td class="column-3">The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.<br>
</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">type <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The object type: <code>"artist"</code><br>
</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">uri</td><td class="column-2">string</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify URI</a> for the artist.</td>
</tr>
</tbody>
</table>



<h2>audio features object</h2>
<table id="tablepress-215" class="tablepress table tablepress-id-215">
<thead>
<tr class="row-1 odd">
	<th class="column-1">Key</th><th class="column-2">Value Type</th><th class="column-3">Value Description</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">acousticness</td><td class="column-2">float</td><td class="column-3">A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">analysis_url</td><td class="column-2">string</td><td class="column-3">An HTTP URL to access the full audio analysis of this track.  An access token is required to access this data. </td>
</tr>
<tr class="row-4 even">
	<td class="column-1">danceability</td><td class="column-2">float</td><td class="column-3">Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.  A value of 0.0 is least danceable and 1.0 is most danceable.  </td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">duration_ms</td><td class="column-2">int</td><td class="column-3">The duration of the track in milliseconds.</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">energy</td><td class="column-2">float</td><td class="column-3">Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">id</td><td class="column-2">string</td><td class="column-3">The Spotify ID for the track. </td>
</tr>
<tr class="row-8 even">
	<td class="column-1">instrumentalness</td><td class="column-2">float</td><td class="column-3">Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">key</td><td class="column-2">int</td><td class="column-3">The key the track is in. Integers map to pitches using standard <a href="https://en.wikipedia.org/wiki/Pitch_class">Pitch Class notation</a>. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">liveness</td><td class="column-2">float</td><td class="column-3">Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">loudness</td><td class="column-2">float</td><td class="column-3">The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of  tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.</td>
</tr>
<tr class="row-12 even">
	<td class="column-1">mode</td><td class="column-2">int</td><td class="column-3">Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived.  Major is represented by 1 and minor is 0.</td>
</tr>
<tr class="row-13 odd">
	<td class="column-1">speechiness</td><td class="column-2">float</td><td class="column-3">Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.</td>
</tr>
<tr class="row-14 even">
	<td class="column-1">tempo</td><td class="column-2">float</td><td class="column-3">The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.</td>
</tr>
<tr class="row-15 odd">
	<td class="column-1">time_signature</td><td class="column-2">int</td><td class="column-3">An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).</td>
</tr>
<tr class="row-16 even">
	<td class="column-1">track_href</td><td class="column-2">string</td><td class="column-3">A link to the Web API endpoint providing full details of the track.</td>
</tr>
<tr class="row-17 odd">
	<td class="column-1">type</td><td class="column-2">string</td><td class="column-3">The object type: "audio_features"</td>
</tr>
<tr class="row-18 even">
	<td class="column-1">uri</td><td class="column-2">string</td><td class="column-3">The Spotify URI for the track. </td>
</tr>
<tr class="row-19 odd">
	<td class="column-1">valence</td><td class="column-2">float</td><td class="column-3">A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).</td>
</tr>
</tbody>
</table>


<h2>track object (full)</h2>
<table id="tablepress-58" class="tablepress table tablepress-id-58">
<thead>
<tr class="row-1 odd">
	<th class="column-1">Key <br>
</th><th class="column-2">Value&nbsp;Type <br>
</th><th class="column-3">Value Description <br>
</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">album <br>
</td><td class="column-2">a simplified <a href="/web-api/object-model/#album-object-simplified">album object</a><br>
</td><td class="column-3">The album on which the track appears. The album object includes a link in <code>href</code> to full information about the album. <br>
</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">artists <br>
</td><td class="column-2">an array of simplified <a href="/web-api/object-model/#artist-object-simplified">artist objects</a></td><td class="column-3">The artists who performed the track. Each artist object includes a link in <code>href</code> to more detailed information about the artist. <br>
</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">available_markets <br>
</td><td class="column-2">array of strings<br>
</td><td class="column-3">A list of the countries in which the track can be played, identified by their<a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"> ISO 3166-1 alpha-2</a> code. <br>
</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">disc_number <br>
</td><td class="column-2">integer<br>
</td><td class="column-3">The disc number (usually <code>1</code> unless the album consists of more than one disc). <br>
</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">duration_ms <br>
</td><td class="column-2">integer<br>
</td><td class="column-3">The track length in milliseconds. <br>
</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">explicit <br>
</td><td class="column-2">Boolean<br>
</td><td class="column-3">Whether or not the track has explicit lyrics (<code>true</code> = yes it does; <code>false</code> = no it does not OR unknown). <br>
</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">external_ids <br>
</td><td class="column-2">an <a href="/web-api/object-model/#external-id-object">external ID object</a></td><td class="column-3">Known external IDs for the track.</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">external_urls</td><td class="column-2">an <a href="/web-api/object-model/#external-url-object">external URL object</a></td><td class="column-3">Known external URLs for this track.</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">href</td><td class="column-2">string</td><td class="column-3">A link to the Web API endpoint providing full details of the track.</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">id <br>
</td><td class="column-2">string</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify ID</a> for the track. <br>
</td>
</tr>
<tr class="row-12 even">
	<td class="column-1">is_playable</td><td class="column-2">boolean</td><td class="column-3">Part of the response when <a href="https://developer.spotify.com/web-api/track-relinking-guide/">Track Relinking</a> is applied. If <code>true</code>, the track is playable in the given market. Otherwise <code>false</code>.</td>
</tr>
<tr class="row-13 odd">
	<td class="column-1">linked_from</td><td class="column-2">a <a href="https://developer.spotify.com/web-api/object-model/#track-link">linked track object</a></td><td class="column-3">Part of the response when <a href="https://developer.spotify.com/web-api/track-relinking-guide/">Track Relinking</a> is applied, and the requested track has been replaced with different track. The track in the <code>linked_from</code> object contains information about the originally requested track.</td>
</tr>
<tr class="row-14 even">
	<td class="column-1">name <br>
</td><td class="column-2">string<br>
</td><td class="column-3">The name of the track.<br>
</td>
</tr>
<tr class="row-15 odd">
	<td class="column-1">popularity <br>
</td><td class="column-2">integer<br>
</td><td class="column-3">The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.<br>
<br>
The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.<br>
<br>
Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. Note that the popularity value may lag actual popularity by a few days: the value is not updated in real time.</td>
</tr>
<tr class="row-16 even">
	<td class="column-1">preview_url <br>
</td><td class="column-2">string<br>
</td><td class="column-3">A link to a 30 second preview (MP3 format) of the track. </td>
</tr>
<tr class="row-17 odd">
	<td class="column-1">track_number <br>
</td><td class="column-2">integer<br>
</td><td class="column-3">The number of the track. If an album has several discs, the track number is the number on the specified disc.</td>
</tr>
<tr class="row-18 even">
	<td class="column-1">type <br>
</td><td class="column-2">string</td><td class="column-3">The object type: "track".<br>
</td>
</tr>
<tr class="row-19 odd">
	<td class="column-1">uri</td><td class="column-2">string</td><td class="column-3">The <a href="/web-api/user-guide/#spotify-uris-and-ids">Spotify URI</a> for the track.</td>
</tr>
</tbody>
</table>
